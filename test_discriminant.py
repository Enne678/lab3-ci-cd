import unittest
from discriminant import calculate_discriminant


class TestDiscriminant(unittest.TestCase):

    def test_positive_discriminant(self):
        """Тест для случая с положительным дискриминантом."""
        self.assertEqual(calculate_discriminant(1, 5, 6), 1)

    def test_zero_discriminant(self):
        """Тест для случая с нулевым дискриминантом."""
        self.assertEqual(calculate_discriminant(1, 2, 1), 0)

    def test_negative_discriminant(self):
        """Тест для случая с отрицательным дискриминантом."""
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)
