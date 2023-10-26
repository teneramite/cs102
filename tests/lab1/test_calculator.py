import unittest
import calculator_made_with_love 

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator_made_with_love.addition(2, 2), 4)
        self.assertEqual(calculator_made_with_love.addition(-2, 2), 0)
        self.assertEqual(calculator_made_with_love.addition(-2, -2), -4)

    def test_subtraction(self):
        self.assertEqual(calculator_made_with_love.subtraction(2, 2), 0)
        self.assertEqual(calculator_made_with_love.subtraction(-2, 2), -4)
        self.assertEqual(calculator_made_with_love.subtraction(-2, -2), 0)

    def test_multiplication(self):
        self.assertEqual(calculator_made_with_love.multiplication(2, 2), 4)
        self.assertEqual(calculator_made_with_love.multiplication(-2, 2), -4)
        self.assertEqual(calculator_made_with_love.multiplication(-2, 0),0 )
        
    def test_division(self):
        self.assertEqual(calculator_made_with_love.division(2, 2), 1)
        self.assertEqual(calculator_made_with_love.division(-2, 2), -1)
        self.assertEqual(calculator_made_with_love.division(1, 2),0.5 )

        with self.assertRaises(ValueError):
            calculator_made_with_love.division(2, 0)

    
            



if __name__ == "__main__":
    unittest.main()
