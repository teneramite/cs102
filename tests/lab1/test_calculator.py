import unittest

from src.lab1.calculator import addition, subtraction, multiplication, division

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 2), 4)
        self.assertEqual(addition(-2, 2), 0)
        self.assertEqual(addition(-2, -2), -4)

    def test_subtraction(self):
        self.assertEqual(subtraction(2, 2), 0)
        self.assertEqual(subtraction(-2, 2), -4)
        self.assertEqual(subtraction(-2, -2), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 2), 4)
        self.assertEqual(multiplication(-2, 2), -4)
        self.assertEqual(multiplication(-2, 0),0 )
        
    def test_division(self):
        self.assertEqual(division(2, 2), 1)
        self.assertEqual(division(-2, 2), -1)
        self.assertEqual(division(1, 2),0.5 )

        with self.assertRaises(ValueError):
            division(2, 0)


if __name__ == "__main__":
    unittest.main()
