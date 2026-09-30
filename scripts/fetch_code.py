"""Preview or fetch a selected pinned, licensed source-only snapshot. Never execute it."""
import argparse
import hashlib
import json
import re
import urllib.request
from pathlib import Path, PurePosixPath
from urllib.parse import quote
from comparison_common import ROOT, read

SOURCE_SUFFIXES = {'.py', '.c', '.h', '.cpp', '.hpp', '.cc', '.m', '.jl', '.r', '.rs', '.js', '.ts', '.sh', '.ps1', '.bat', '.f', '.f90', '.cu', '.cuh'}
BLOCKED_PARTS = {'models', 'model', 'weights', 'checkpoints', 'datasets', 'dataset', 'data', 'results', '.git', '.idea', '.venv', 'venv', 'node_modules', 'secrets', 'credentials'}
MAX_FILE_BYTES = 1024 * 1024
MAX_TOTAL_BYTES = 20 * 1024 * 1024


def selected_path(path, licenses, readme):
    parts = PurePosixPath(path)
    if parts.is_absolute() or '..' in parts.parts or '\\' in path or ':' in path:
        return False
    if any(p.lower() in BLOCKED_PARTS for p in parts.parts):
        return False
    base = parts.name.lower()
    if base.startswith('.') or any(x in base for x in ('credential', 'secret', 'token', 'password')):
        return False
    return path in licenses or path == readme or parts.suffix.lower() in SOURCE_SUFFIXES


def get(url, limit=MAX_FILE_BYTES):
    request = urllib.request.Request(url, headers={'User-Agent': 'awesome-cryptanalytic-extraction-source-collector'})
    with urllib.request.urlopen(request, timeout=30) as response:
        value = response.read(limit + 1)
    if len(value) > limit:
        raise ValueError(f'Size limit exceeded: {url}')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--paper', required=True, help='Select exactly one catalog paper ID')
    parser.add_argument('--fetch', action='store_true', help='Download selected source text; default is a no-network preview')
    args = parser.parse_args()
    audit = read('code/source-audit.json')
    papers = {p['paper_id']: p for p in audit['papers']}
    if args.paper not in papers:
        parser.error('Unknown paper ID')
    paper = papers[args.paper]
    repo = next((r for r in audit['repositories'] if r['id'] == paper.get('repository_id')), None)
    if not repo or repo.get('access') != 'accessible' or repo.get('kind') in {'reading_resource', 'placeholder_repository'}:
        parser.error('No accessible pinned implementation/artifact; use the audited reference index')
    pin = repo.get('commit', '')
    if not re.fullmatch(r'[a-f0-9]{40}', pin):
        parser.error('Fixed commit required')
    print(json.dumps({'paper_id': args.paper, 'upstream': repo['url'], 'commit': pin,
                      'license': repo['license'], 'artifact_kind': repo['kind'], 'mode': 'fetch' if args.fetch else 'dry-run'}, indent=2))
    if not args.fetch:
        print('No network requests or filesystem writes. Add --fetch for licensed source-only collection.')
        return
    if repo['license'].get('status') != 'declared_license_verified' or not repo['license'].get('license_files'):
        parser.error('No verified project license: retained as a source pointer; no source files copied')
    tree_url = f'https://api.github.com/repos/{repo["id"]}/git/trees/{pin}?recursive=1'
    tree = json.loads(get(tree_url, MAX_TOTAL_BYTES))
    if tree.get('truncated'):
        raise ValueError('Incomplete upstream tree; refusing a partial licensing/source audit')
    licenses = set(repo['license']['license_files'])
    candidates = [entry for entry in tree['tree'] if entry['type'] == 'blob'
                  and entry.get('mode') != '120000'
                  and entry.get('size', MAX_FILE_BYTES + 1) <= MAX_FILE_BYTES
                  and selected_path(entry['path'], licenses, repo.get('readme_path'))]
    selected_names = {entry['path'] for entry in candidates}
    if not licenses.issubset(selected_names):
        raise ValueError('Required license files excluded or unavailable; no snapshot created')
    if sum(entry['size'] for entry in candidates) > MAX_TOTAL_BYTES:
        raise ValueError('Selected source snapshot exceeds total size limit')
    destination = ROOT / 'code/downloads' / args.paper / pin
    if destination.exists():
        raise ValueError(f'Destination already exists; keep the existing snapshot: {destination}')
    fetched = []
    total = 0
    # Obtain and verify all files before writing any partial snapshot.
    for entry in candidates:
        url = f'https://raw.githubusercontent.com/{repo["id"]}/{pin}/{quote(entry["path"], safe="/")}'
        content = get(url)
        total += len(content)
        if total > MAX_TOTAL_BYTES:
            raise ValueError('Total download limit exceeded')
        digest = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
        if digest != entry['sha']:
            raise ValueError(f'Git blob hash mismatch: {entry["path"]}')
        if b'\0' in content:
            raise ValueError(f'Binary content in source snapshot: {entry["path"]}')
        content.decode('utf-8')
        fetched.append((entry['path'], content))
    for path, content in fetched:
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    receipt = {'paper_id': args.paper, 'repository': repo['url'], 'commit': pin, 'license': repo['license'],
               'files': [{'path': path, 'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)} for path, content in fetched],
               'not_executed': True, 'excluded': 'weights, datasets, binary files, notebooks, submodules, credential paths'}
    (destination / 'COLLECTION_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(f'Fetched {len(fetched)} source/documentation/license files ({total} bytes); nothing executed: {destination}')


if __name__ == '__main__':
    main()
