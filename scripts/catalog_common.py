"""Work identities shared by catalog validation and duplicate screening."""
import re
import unicodedata
from urllib.parse import unquote, urlparse


def normalized_title(title):
    text = unicodedata.normalize('NFKD', title).casefold()
    return ''.join(c for c in text if c.isalnum())


def normalized_identity(value):
    value = unquote(value).strip().casefold()
    arxiv = re.fullmatch(r'(?:arxiv[: -]?)?(\d{4}\.\d{4,5})(?:v\d+)?', value)
    eprint = re.fullmatch(r'(?:iacr[ :/-]*)?(?:eprint[ :/-]*)?(\d{4})[/-](\d+)', value)
    if arxiv:
        return 'arxiv:' + arxiv[1]
    if eprint:
        return 'eprint:' + eprint[1] + '/' + str(int(eprint[2]))
    value = re.sub(r'^doi:\s*', '', value)
    if value.startswith('10.'):
        value = 'https://doi.org/' + value
    parsed = urlparse(value)
    host = (parsed.hostname or '').removeprefix('www.')
    path = parsed.path.rstrip('/')
    if host in {'arxiv.org', 'export.arxiv.org'}:
        match = re.fullmatch(r'/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?', path)
        if match:
            return 'arxiv:' + match[1]
    if host in {'eprint.iacr.org', 'ia.cr'}:
        match = re.fullmatch(r'/(\d{4})/(\d+)(?:\.pdf)?', path)
        if match:
            return 'eprint:' + match[1] + '/' + str(int(match[2]))
    if host in {'doi.org', 'dx.doi.org'}:
        match = re.fullmatch(r'/10\.48550/arxiv\.(\d{4}\.\d{4,5})(?:v\d+)?', path)
        return 'arxiv:' + match[1] if match else 'doi:' + path.lstrip('/')
    return 'url:' + host + path if host else value


def identity_keys(paper):
    values = [paper['url'], *paper.get('aliases', [])]
    values += [paper[key] for key in ('doi', 'arxiv_id', 'eprint_id', 'canonical_url') if paper.get(key)]
    return {'title:' + normalized_title(paper['title']), *(normalized_identity(v) for v in values)}


def validate_identities(papers):
    owners = {}
    for paper in papers:
        for key in identity_keys(paper):
            assert key not in owners or owners[key] == paper['id'], (key, owners.get(key), paper['id'])
            owners[key] = paper['id']
    return owners
