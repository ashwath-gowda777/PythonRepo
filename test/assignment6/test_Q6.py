import unittest
from src.assignment6.util import print_formatted

class TestPrintFormatted(unittest.TestCase):
    def test_print_formatted(self):
        with self.assertRaises(SystemExit):
            print_formatted(5)

if __name__ == '__main__':
    unittest.main()

