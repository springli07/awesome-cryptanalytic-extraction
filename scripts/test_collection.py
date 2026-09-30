"""Offline guardrail checks: no upstream code/network is used."""
import unittest
from fetch_code import selected_path
from comparison_common import validate_metric


class CollectionChecks(unittest.TestCase):
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
