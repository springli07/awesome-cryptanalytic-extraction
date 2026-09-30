"""Merge reviewed research records by paper ID without changing the bibliography."""
import argparse
from comparison_common import ROOT, METRICS, read, records, write, validate_comparisons


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputs', nargs='+', help='Research JSON paths relative to repository root')
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    catalog = read('data/papers.json')
    result = {}
    for filename in args.inputs:
        for record in records(read(filename)):
            paper_id = record['paper_id']
            assert paper_id not in result, f'duplicate research record: {paper_id}'
            result[paper_id] = record
    assert set(result) == {p['id'] for p in catalog['papers']}, 'missing/unknown paper IDs'
    data = {'schema_version': 1, 'checked': catalog['updated'], 'scope': 'Stage costs; no independent reproduction',
            'metric_types': list(METRICS), 'papers': [result[p['id']] for p in catalog['papers']]}
    validate_comparisons(data, strict=args.strict)
    write('data/comparisons.json', data)
    print(f'Merged {len(result)} reviewed comparison records.')


if __name__ == '__main__':
    main()
