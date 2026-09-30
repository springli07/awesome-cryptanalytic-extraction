"""Validate complete evidence coverage, pinned source mappings and generated documents."""
import argparse
import configparser
import re
import subprocess
import sys
from urllib.parse import urlparse, unquote
from comparison_common import ROOT, read, validate_comparisons


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true', help='Reject unfinished reviews')
    args = parser.parse_args()
    catalog = read('data/papers.json')
    data = read('data/comparisons.json')
    count = validate_comparisons(data, strict=args.strict)
    expected = {p['id'] for p in catalog['papers']}
    audit = read('code/source-audit.json')
    assert len(audit['papers']) == count
    assert {p['paper_id'] for p in audit['papers']} == expected
    repos = {r['id']: r for r in audit['repositories']}
    assert len(repos) == len(audit['repositories'])
    for paper in audit['papers']:
        assert paper.get('provenance'), paper['paper_id']
        if paper.get('repository_id'):
            assert paper['repository_id'] in repos
    for repo in repos.values():
        if repo['access'] == 'accessible':
            assert re.fullmatch(r'[a-f0-9]{40}', repo['commit']), repo['id']
        assert repo.get('license') and repo.get('kind'), repo['id']
    links = subprocess.check_output(['git', 'ls-files', '--stage', 'code/upstream', 'code/artifacts'], cwd=ROOT, text=True)
    indexed = {}
    for line in links.splitlines():
        metadata, path = line.split('\t', 1)
        mode, commit, stage = metadata.split()
        assert mode == '160000' and stage == '0', path
        indexed[path] = commit
    modules = configparser.ConfigParser()
    modules.read(ROOT / '.gitmodules', encoding='utf-8')
    declared = {modules[s]['path']: modules[s]['url'] for s in modules.sections()}
    assert set(declared) == set(indexed), 'Gitmodule declarations differ from gitlinks'
    for path, commit in indexed.items():
        repository_id = path.split('/', 2)[2]
        repo = repos[repository_id]
        assert commit == repo['commit'], path
        assert declared[path] == repo['url'] + '.git', path
        assert repo['kind'] not in ('reading_resource', 'placeholder_repository'), path
    for paper in audit['papers']:
        manifest = read('code/manifests/' + paper['paper_id'] + '.json')
        assert manifest['paper_id'] == paper['paper_id']
        if manifest.get('collection_path'):
            assert indexed[manifest['collection_path']] == manifest['pinned_commit'], paper['paper_id']
        if paper.get('repository_id'):
            assert manifest['pinned_commit'] == repos[paper['repository_id']].get('commit'), paper['paper_id']
        assert manifest['code_executed'] is False and manifest['scientifically_reproduced'] is False
    subprocess.run([sys.executable, str(ROOT / 'scripts/render_comparisons.py'), '--check'], check=True)
    files = [ROOT / 'docs/comparison_en.md', ROOT / 'docs/comparison_zh.md', ROOT / 'code/README.md', ROOT / 'code/README_zh-CN.md', *sorted((ROOT / 'docs/comparisons').glob('*.md'))]
    for path in files:
        text = path.read_text(encoding='utf-8')
        assert '\ufffd' not in text, path
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if not urlparse(link).scheme and not link.startswith('#'):
                assert (path.parent / unquote(link.split('#')[0])).exists(), (path, link)
    print(f'PASS: {count} evidence-backed comparison records, {len(repos)} code sources, {len(indexed)} pinned gitlinks and bilingual documents.')


if __name__ == '__main__':
    main()
