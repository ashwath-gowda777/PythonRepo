import unittest
from src.assignment3.util import runner_up_score

class TestRunnerUpScore(unittest.TestCase):
    def test_runner_up_score(self):
        # Example test case
        values = [1, 2, 3, 4]
        expected_result = 3  # The second-to-last element after sorting is 3
        result = runner_up_score(values)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

