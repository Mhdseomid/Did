import unittest
from add import add_numbers

class TestAddNum(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(5, 10), 15)
        self.assertEqual(add_numbers(0, 5), 5)

   

