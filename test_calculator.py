import unittest
import test_branch as calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(3, 2), 1)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 2), 6)
        self.assertEqual(calculator.multiply(1, 0), 0)
        self.assertEqual(calculator.multiply(-1, -1), 1)
        self.assertEqual(calculator.multiply(-1, 5), -5)
        self.assertEqual(calculator.multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.divide(1, 1), 1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()