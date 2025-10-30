import unittest
from discriminant import calculate_discriminant

class TestDiscriminant(unittest.TestCase):
    
    def test_positive_discriminant(self):
        # D > 0 - два корня
        self.assertEqual(calculate_discriminant(1, 5, 6), 1)
        self.assertEqual(calculate_discriminant(2, 7, 3), 25)
    
    def test_zero_discriminant(self):
        # D = 0 - один корень
        self.assertEqual(calculate_discriminant(1, 2, 1), 0)
    
    def test_negative_discriminant(self):
        # D < 0 - нет действительных корней
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)