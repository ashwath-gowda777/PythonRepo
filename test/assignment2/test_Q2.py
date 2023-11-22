import unittest
from src.assignment2.util import total_marks

class TestListCommands(unittest.TestCase):
    def test_total_marks(self):
        # Example test case
        student_cgpa = {"Ashwath": [7.0, 8.0, 9.0], "Tilak": [7.0, 8.0, 6.0]}
        student = "Tilak"
        output = 7
        result = total_marks(student_cgpa, student)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()