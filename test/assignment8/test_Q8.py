import unittest
from src.assignment8.util import day_name

class TestGetDayName(unittest.TestCase):

    def test_Now_Testing_is_done(self):
        self.assertEqual(day_name(11, 23, 2023), "THURSDAY")


if __name__ == '__main__':
    unittest.main()