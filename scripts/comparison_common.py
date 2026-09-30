"""Shared evidence validation and serialization for the comparison catalog."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = ('theoretical_queries', 'arithmetic', 'experimental_queries', 'runtime')


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def write(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def records(data):
    if isinstance(data, list):
        return data
    return data.get('papers', data.get('records', []))


def validate_metric(metric, label):
    assert isinstance(metric, dict), label
    assert metric.get('status') in {'reported', 'derived', 'NR', 'NA', 'pending'}, label
    status = metric['status']
    if status == 'pending':
        return
    assert metric.get('evidence'), f'{label}: evidence required even for NR/NA'
    if status in {'reported', 'derived'}:
        assert metric.get('value') is not None and metric.get('unit'), label
    if status == 'derived':
        assert metric.get('premises') or metric.get('derivation'), f'{label}: derivation premises required'
    for evidence in metric['evidence']:
        assert evidence.get('url', '').startswith('https://'), label
        assert evidence.get('locator'), f'{label}: section/theorem/page/code locator required'
        fingerprint = evidence.get('pdf_sha256')
        if fingerprint:
            assert re.fullmatch(r'[a-f0-9]{64}', fingerprint), label
        if evidence.get('kind') == 'code':
            assert re.fullmatch(r'[a-f0-9]{40}', evidence.get('commit', '')), label


def validate_comparisons(data, strict=False):
    papers = read('data/papers.json')['papers']
    expected = {p['id'] for p in papers}
    rows = records(data)
    assert {p['paper_id'] for p in rows} == expected, 'comparison coverage must match entire catalog'
    assert len(rows) == len(expected), 'duplicate comparison paper ID'
    for paper in rows:
        assert paper.get('stages'), paper['paper_id']
        for stage in paper['stages']:
            metrics = stage.get('metrics', stage)
            for key in METRICS:
                assert key in metrics, f'{paper["paper_id"]}: missing {key}'
                validate_metric(metrics[key], f'{paper["paper_id"]}/{stage.get("name", "stage")}/{key}')
                if strict:
                    assert metrics[key]['status'] != 'pending', f'{paper["paper_id"]}: pending metric'
        if strict:
            assert paper.get('review_status') == 'source-reviewed', paper['paper_id']
        for experiment in paper.get('experiments', []):
            assert experiment.get('dimensions') and experiment.get('target'), paper['paper_id']
            for key in ('experimental_queries', 'runtime'):
                validate_metric(experiment[key], f'{paper["paper_id"]}/experiment/{key}')
    return len(rows)
