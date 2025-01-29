import unittest
from demo_script import find_even_numbers

class TestFindEvenNumbers(unittest.TestCase):
    def test_all_even(self):
        numbers = [2, 4, 6, 8, 10]
        even_numbers, even_count = find_even_numbers(numbers)
        self.assertEqual(even_numbers, [2, 4, 6, 8, 10])
        self.assertEqual(even_count, 5)

    def test_all_odd(self):
        numbers = [1, 3, 5, 7, 9]
        even_numbers, even_count = find_even_numbers(numbers)
        self.assertEqual(even_numbers, [])
        self.assertEqual(even_count, 0)

    def test_mixed(self):
        numbers = [1, 2, 3, 4, 5, 6]
        even_numbers, even_count = find_even_numbers(numbers)
        self.assertEqual(even_numbers, [2, 4, 6])
        self.assertEqual(even_count, 3)

    def test_empty(self):
        numbers = []
        even_numbers, even_count = find_even_numbers(numbers)
        self.assertEqual(even_numbers, [])
        self.assertEqual(even_count, 0)

if __name__ == '__main__':
    unittest.main()