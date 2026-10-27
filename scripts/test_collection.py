"""Offline guardrail checks: no upstream code/network is used."""
import unittest
from fetch_code import selected_path
from comparison_common import validate_metric
from catalog_common import normalized_identity, normalized_title, validate_identities


class CollectionChecks(unittest.TestCase):
    def test_work_identity_normalization(self):
        self.assertEqual(normalized_title('ReLU: Sign-Recovery'), normalized_title('relu sign recovery'))
        for value in ('http://arxiv.org/abs/2609.35487v1', 'https://arxiv.org/pdf/2609.35487v2.pdf',
                      'https://doi.org/10.48550/arXiv.2609.35487'):
            self.assertEqual(normalized_identity(value), 'arxiv:2609.35487')
        for value in ('https://eprint.iacr.org/2026/2097.pdf?download=1', 'https://ia.cr/2026/2097/'):
            self.assertEqual(normalized_identity(value), 'eprint:2026/2097')
        self.assertEqual(normalized_identity('doi:10.1007/example'), normalized_identity('https://dx.doi.org/10.1007/example'))
        paper = {'id': 'one', 'title': 'First title', 'url': 'https://arxiv.org/abs/2609.35487', 'aliases': []}
        duplicate = {'id': 'two', 'title': 'Different title', 'url': 'https://doi.org/10.48550/arXiv.2609.35487', 'aliases': []}
        with self.assertRaises(AssertionError):
            validate_identities([paper, duplicate])
        for duplicate in (
            {'id': 'two', 'title': 'FIRST TITLE!', 'url': 'https://example.org/other'},
            {'id': 'two', 'title': 'Other title', 'url': 'https://example.org/other',
             'aliases': ['https://arxiv.org/pdf/2609.35487v1']},
        ):
            with self.assertRaises(AssertionError):
                validate_identities([paper, duplicate])

    def test_excludes_weights_data_symlinks_and_traversal(self):
        for path in ['../attack.py', '/attack.py', 'C:/attack.py', 'models/train.py', 'data/samples.py',
                     'src/token.py', 'weights/model.pt', '.env', 'notebook.ipynb', 'src/binary.dll']:
            self.assertFalse(selected_path(path, set(), 'README.md'), path)
        for path in ['src/extract.py', 'LICENSE', 'README.md']:
            self.assertTrue(selected_path(path, {'LICENSE'}, 'README.md'), path)

    def test_cost_requires_locator_and_derived_premises(self):
        with self.assertRaises(AssertionError):
            validate_metric({'status': 'reported', 'value': 'O(n)', 'unit': 'calls', 'evidence': [{'url': 'https://example.org'}]}, 'test')
        with self.assertRaises(AssertionError):
            validate_metric({'status': 'derived', 'value': '0', 'unit': 'calls', 'evidence': [{'url': 'https://example.org', 'locator': 'Algorithm 1'}]}, 'test')


if __name__ == '__main__':
    unittest.main()
