import unittest
from equation import calculate_y

class TestEquationTask(unittest.TestCase):
    
    def test_normal_case(self):
        result = calculate_y(a = 10, b = 1, c = 5, d = 2)
        self.assertEqual(result, 1.0)
    
    def test_zero_numerator(self):
        result = calculate_y(a = 4, b = 4, c = 3, d = 1)
        self.assertEqual(result, 0.0)

    def test_negative_root_value_error(self):
        with self.assertRaises(ValueError):
            calculate_y(a = 1, b = 5, c = 3, d = 1)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_y(a = 5, b = 1, c = 2, d = 2)

if __name__ == '__main__':
    unittest.main()