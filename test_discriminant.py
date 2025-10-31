import unittest
from discriminant import calculate_discriminant


class TestDiscriminant(unittest.TestCase):
    
    # Положительные тесты (D >= 0)
    def test_positive_discriminant(self):
        result = calculate_discriminant(1, 5, 6)
        self.assertEqual(result, 1)
    
    def test_zero_discriminant(self):
        result = calculate_discriminant(1, 2, 1)
        self.assertEqual(result, 0)
    
    # Негативные тесты (D < 0)
    def test_negative_discriminant(self):
        result = calculate_discriminant(1, 1, 1)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()
    