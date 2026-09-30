"""Build pinned Git pointers only; never download or execute upstream code."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROWS = '''ftramer/Steal-ML e37c67b2f74e42a85370ce431bc9d4e391b0ed8b implementation
google-research/cryptanalytic-model-extraction 1093b6212f7018b1c14e24c80edb56ac05c0777c implementation
Crypto-TII/deti e411fbc28225a7d627cf2eebd57a92812104bf2b implementation
hannafoe/cryptanalytical-extraction 4280cd6770560fa717e6e8b4d337a29ba8bba77c implementation
PsyduckLiu/End-to-End-Deep-Neural-Network-Extraction 5206db797c123136aad21f69e7e01aeb15c2d9e0 implementation
1983321048/Geometric-Critical-Point-Screening 595fce480e82dab009c185e41f233fc477a6cc15 implementation
AI-Lab-Y/NN_cryptanalytic_extraction f363700ff141a8e0f81c68fb18ce703897884fc5 verification_artifact
Jchavezsaab/hard-label-dnn-extraction 2a450eb5096d99cb8cf9ac99c00c13f721071890 implementation
deividafonso281/hard-label-contract-output 0d137df322000eb07d7082497e83f6c07d3f00a8 supplementary_implementation
PsyduckLiu/Model-Extraction-of-CNNs-with-Max-Pooling 56cb180d255df2a8d8af8766378b2ec490611d3a implementation
AI-Lab-Y/Extracting_PReLU_NN d724ce37dac9a119ec388f241a9341a7650785d7 implementation
qixiaokang1-stack/cryptanalytic-model-various-functions 2d3a9dbff314d620fe1e33ac09d0f84ae87149fb implementation
mstealercryptocrypto-ops/mod_stealer26 95a5cd29bc23f3ce38a99802e0c6e2891ce3ef2d implementation
springli07/GNN_MP_CEA dde7f7e529a39eaa219924a4ec11e2ceab37c6e7 implementation
dpaleka/stealing-part-lm-supplementary 6fa1d1a87b06e00228330711eb661cee58b4740d supplementary_implementation
bcoqueret/Side_channel_cryptanalytic_extraction_of_DNN 8a729158d83adf587e2d2444e6587a2f489603b9 simulation_artifact
heavyimage/afch_paper 1b5d035d1f13de4ded4c1e435de7301f16c3c983 implementation
anonymous-123-code/anonymouscode 2092c04718d81c69dfcba88702f0c6b6dcd70b3f implementation
flavio-martinelli/expand-and-cluster 231cac970ceef43cb6361cd39917d75e44d7776e implementation
alexl4123/expand-and-cluster 07edef32b213f7a56a1fd66249e6f6b8207aabbf author_extension_fork'''

def main():
    catalog = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    audit_path = ROOT / 'code/source-audit.json'
    audit = json.loads(audit_path.read_text(encoding='utf-8')) if audit_path.exists() else None
    rows = {r[0]: {'commit': r[1], 'kind': r[2]} for r in (line.split() for line in ROWS.splitlines())}
    modules = []
    for repo, row in rows.items():
        base = 'artifacts' if row['kind'] in ('verification_artifact', 'simulation_artifact') else 'upstream'
        path = f'code/{base}/{repo}'
        row['path'] = path
        (ROOT / path).mkdir(parents=True, exist_ok=True)
        modules.append(f'[submodule "{path}"]\n\tpath = {path}\n\turl = https://github.com/{repo}.git\n')
        subprocess.run(['git', 'update-index', '--add', '--cacheinfo', f"160000,{row['commit']},{path}"], cwd=ROOT, check=True)
    (ROOT / '.gitmodules').write_text('\n'.join(modules), encoding='utf-8')
    out = ROOT / 'code/manifests'
    out.mkdir(parents=True, exist_ok=True)
    audit_papers = {p['paper_id']: p for p in audit['papers']} if audit else {}
    audit_repos = {r['id']: r for r in audit['repositories']} if audit else {}
    for p in catalog['papers']:
        ap = audit_papers.get(p['id'], {})
        url = ap.get('source_url') or p['code'].get('url')
        repo = ap.get('repository_id') or (url.split('github.com/')[1].rstrip('/') if url and url.startswith('https://github.com/') else None)
        row = rows.get(repo)
        record = {'schema_version': 1, 'paper_id': p['id'], 'title': p['title'], 'audit_ref': '../source-audit.json', 'source_url': url, 'repository_id': repo, 'status': ap.get('status', p['code']['status']), 'pinned_commit': row['commit'] if row else None, 'collection_path': row['path'] if row else None, 'code_executed': False, 'scientifically_reproduced': False}
        if p['id'] == 'eprint-2026-1025':
            record['paper_status'] = 'withdrawn'
            record['note'] = 'Historical artifact only; paper withdrawn on 2026-09-19.'
        if repo in audit_repos:
            record['pinned_commit'] = audit_repos[repo].get('commit')
            record['source_url'] = audit_repos[repo]['url']
        (out / f"{p['id']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f"Created {len(rows)} pinned gitlinks and {len(catalog['papers'])} paper manifests; no upstream checkout/download/execution.")

if __name__ == '__main__':
    main()
