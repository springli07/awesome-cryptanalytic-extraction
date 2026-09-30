"""Generate bilingual navigation, stage tables, and original-code collection index."""
import argparse
from collections import Counter
from comparison_common import ROOT, METRICS, read, records, validate_comparisons


def esc(value):
    return str(value).replace('|', '&#124;').replace('\n', '<br>')


def label(value, lang):
    return value.get(lang, value.get('en', value.get('zh', ''))) if isinstance(value, dict) else str(value)


def metric_text(metric):
    status = metric['status']
    value = str(metric['value']) if metric.get('value') is not None else status
    if status == 'derived':
        value = 'Derived / 推导: ' + value
    if metric.get('unit'):
        value += ' [' + metric['unit'] + ']'
    reason = metric.get('reason', metric.get('NR_reason', metric.get('NA_reason')))
    if reason:
        value += '<br>' + str(reason)
    evidence = metric.get('evidence', [])
    if evidence:
        value += '<br>' + '; '.join(f'[{esc(e["locator"])}]({e["url"]})' for e in evidence)
    return esc(value).replace('&#124;', '&#124;')


def comparison(data, catalog, lang):
    zh = lang == 'zh'
    by_id = {r['paper_id']: r for r in records(data)}
    prefix = 'comparison_zh.md' if zh else 'comparison_en.md'
    text = ['# ' + ('逐阶段横向对比' if zh else 'Comparison of stage costs'), '',
            '[English](comparison_en.md) · [中文](comparison_zh.md) · [Catalog](../README.md) · [原代码 / Original code](../code/README.md)', '',
            f'**{len(by_id)} papers / 篇 · {len(catalog["categories"])} categories / 类 · checked {data["checked"]}.**', '',
            'NR = reviewed but not reported / 已核查未报告；NA = not applicable / 不适用；Derived = explicit inference / 明示推导。', '',
            'Compare only equal oracles, targets, dimensions, precision and assumptions. Critical/dual points, samples, API calls, node responses and full-sequence responses are separate units. Arithmetic operations are not wall-clock or bit complexity. Stage reuse does not remove upstream acquisition costs. Sampled fidelity is not certified equivalence.', '',
            '只在预言机、目标、尺寸、精度和假设相同时比较。临界点、双点、样本、API调用、节点响应和完整序列响应分别计量；算术次数不等于墙钟或位复杂度。复用阶段仍须计入前期获取成本，采样保真不认证严格等价。', '',
            '## Full source-reviewed group reports / 分组完整证据', '',
            '- [Foundations + raw outputs / 基础及原始输出](comparisons/raw.zh.md)',
            '- [Hard-label + CNN / 仅标签及CNN](comparisons/hard-cnn.zh.md)',
            '- [Activations, recurrent, attention, GLU and partial LLM / 扩展架构](comparisons/architecture.zh.md)',
            '- [PPML, side channels, precision, defenses, theory and surveys / 上下文](comparisons/context.zh.md)', '',
            'The full reviewed reports above preserve experimental protocols, failure cases, hardware and version caveats. The tables below summarize stage costs; they are not a speed leaderboard. / 完整稿保留实验协议、失败结果、硬件与版本限制；下表为阶段摘要，不是速度排行榜。', '']
    for category in catalog['categories']:
        group = [p for p in catalog['papers'] if p['category'] == category['id']]
        text += [f'## {category[lang]} ({len(group)})', '']
        for paper in group:
            row = by_id[paper['id']]
            text += [f'### {paper["id"]}: [{paper["title"]}]({paper["url"]})', '',
                     f'Oracle / 预言机: {esc(row.get("oracle", paper["oracle"]))}.', '',
                     f'Scope / 范围: {esc(row.get("scope", row.get("target_scope", paper["summary_" + lang])))}', '']
            if paper.get('publication_state') == 'withdrawn':
                text += ['**WITHDRAWN 2026-09-19 / 已撤回；以下仅为历史版本声明。**', '']
            assumptions = row.get('assumptions', row.get('conditioning_assumptions', row.get('conditions')))
            if assumptions:
                text += ['Assumptions / 假设: ' + esc(assumptions), '']
            text += ['| Stage / 阶段 | Theoretical Q / 理论查询 | Arithmetic / 算术 | Experimental Q / 实验查询 | Runtime / 时间 |', '|---|---|---|---|---|']
            for stage in row['stages']:
                metrics = stage.get('metrics', stage)
                stage_label = label(stage['name'], lang)
                for key in ('dimensions', 'precision', 'hardware', 'target', 'notes'):
                    if stage.get(key):
                        stage_label += '<br>' + key + ': ' + str(stage[key])
                text += ['| ' + esc(stage_label) + ' | ' + ' | '.join(metric_text(metrics[k]) for k in METRICS) + ' |']
            text += ['']
            if row.get('experiments'):
                text += ['| Experiment context / 实验设置 | Q | Runtime / 时间 | Metric and limits / 指标及边界 |', '|---|---|---|---|']
                for experiment in row['experiments']:
                    context = '; '.join(f'{k}: {experiment[k]}' for k in ('dimensions', 'precision', 'hardware', 'target') if experiment.get(k))
                    limits = str(experiment.get('empirical_metric', '')) + '<br>' + str(experiment.get('notes', ''))
                    text += [f'| {esc(context)} | {metric_text(experiment["experimental_queries"])} | {metric_text(experiment["runtime"])} | {esc(limits)} |']
                text += ['']
    return '\n'.join(text) + '\n'


def code_index(audit, catalog, lang):
    repos = {r['id']: r for r in audit['repositories']}
    text = ['# ' + ('原代码统一入口' if lang == 'zh' else 'Original code collection'), '',
            '[English](README.md) · [中文](README_zh-CN.md) · [Comparisons / 对比](../docs/comparison_en.md)', '',
            f'**{len(audit["papers"])} papers; {len(repos)} unique GitHub sources.** Checked {audit["checked"]}.', '',
            'Fixed gitlinks under `upstream/` and `artifacts/` point to original authors’ commits; source code is not copied into this repository’s history. Reading lists, placeholders, inaccessible sources and unverified anonymous attachments are indexed separately. Repository availability does not imply reproduction. / 固定gitlink指向原作者提交，不复制源码进主历史；阅读清单、占位、失效和匿名来源另行标记，代码存在不等于复现。', '',
            'Use `python scripts/fetch_code.py --paper PAPER_ID` from the repository root to preview collection; add `--fetch` for a selected, licensed source-only snapshot in ignored `code/downloads/`. The script does not download model weights or datasets, install dependencies or run upstream scripts. Public visibility is not a redistribution license. / 默认仅预览；明确加 --fetch 才下载有许可证的选定源码快照，不下载权重/数据、不安装或运行代码。', '',
            'Git submodules remain browseable source pointers. A full recursive clone may bring upstream models/data; prefer the source-only collector when these are unwanted. Existing upstream licenses and citations apply independently. / 完整递归clone可能拉取上游权重或数据，推荐仅源码收集器；许可证与作者归属仍适用。', '',
            '| Paper ID | Artifact status / 类型 | Fixed source / 固定来源 | License / 许可证 |', '|---|---|---|---|']
    for paper in audit['papers']:
        repo = repos.get(paper.get('repository_id'))
        url = paper.get('source_url')
        license_label = 'unverified'
        if repo:
            commit = repo.get('commit')
            url = repo['url'] + ('/tree/' + commit if commit else '')
            license_label = repo['license'].get('spdx_id') or repo['license']['status']
        source = f'[{esc(repo["id"] if repo else url)}]({url})' if url else 'Not located / 未找到'
        text += [f'| {paper["paper_id"]} | {esc(paper["status"])} | {source} | {esc(license_label)} |']
    text += ['', '## Upstream notes / 原始实现边界', '']
    for repo in audit['repositories']:
        text += [f'### {repo["id"]}', '', f'Commit: `{repo.get("commit") or "unavailable"}` · {repo["kind"]}', '', repo.get('note', ''), '']
        license_evidence = repo['license'].get('evidence_url')
        if license_evidence:
            text += [f'[Pinned license / 固定版本许可证]({license_evidence})', '']
        if repo.get('readme_path') and repo.get('commit'):
            text += [f'[Upstream documentation / 上游文档]({repo["url"]}/blob/{repo["commit"]}/{repo["readme_path"]})', '']
    return '\n'.join(text) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    catalog, data, audit = read('data/papers.json'), read('data/comparisons.json'), read('code/source-audit.json')
    validate_comparisons(data)
    outputs = {'docs/comparison_en.md': comparison(data, catalog, 'en'), 'docs/comparison_zh.md': comparison(data, catalog, 'zh'),
               'code/README.md': code_index(audit, catalog, 'en'), 'code/README_zh-CN.md': code_index(audit, catalog, 'zh')}
    for filename, content in outputs.items():
        target = ROOT / filename
        if args.check:
            assert target.exists() and target.read_text(encoding='utf-8') == content, f'Regenerate {filename}'
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
    print(f'{"Validated" if args.check else "Rendered"} comparisons and original-code index for {len(catalog["papers"])} papers.')


if __name__ == '__main__':
    main()
