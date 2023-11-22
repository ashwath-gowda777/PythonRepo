import unittest
from src.assignment3.util import print_pattern

class TestPrintPattern(unittest.TestCase):

    def test_print_pattern(self):
        thickness = 3
        expected_output = [
            '  H  ',
            ' HHH ',
            'HHHHH',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            '            HHHHH ',
            '             HHH  ',
            '              H   ',
        ]

        # Call the function and compare the result with the corrected expected output
        result = print_pattern(thickness, c='H')
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()