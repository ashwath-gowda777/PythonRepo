import unittest
from src.assignment4.util import mutate_string

class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        input_string = "asdfghj"
        mutation_position = 5
        mutation_character = "k"

        mutated_result = mutate_string(input_string, mutation_position, mutation_character)
        output = "asdfgkj"

        self.assertEqual(mutated_result, output)

if __name__ == '__main__':
    unittest.main()
