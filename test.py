import unittest
import main

class TestCalcu(unittest.TestCase):

    def test_add(self):
        result1 = main.add(5, 3)
        self.assertEqual(result1, 8)

        result2 = main.add(-3, 5)
        self.assertEqual(result2, 2)

        result3 = main.add(-3, -5)
        self.assertEqual(result3, -8)

    def test_subtract(self):
        result1 = main.subtract(5, 3)
        self.assertEqual(result1, 2)

        result2 = main.subtract(-3, 5)
        self.assertEqual(result2, -8)

        result3 = main.subtract(-3, -5)
        self.assertEqual(result3, 2)

    def test_multiply(self):
        result1 = main.multiply(5, 3)
        self.assertEqual(result1, 15)

        result2 = main.multiply(-3, 5)
        self.assertEqual(result2, -15)

        result3 = main.multiply(-3, -5)
        self.assertEqual(result3, 15)

    def test_divide(self):
        result1 = main.divide(5, 3)
        self.assertAlmostEqual(result1, 1.6666666666666667)

        result2 = main.divide(-3, 5)
        self.assertEqual(result2, -0.6)

        result3 = main.divide(-3, -5)
        self.assertEqual(result3, 0.6)

        with self.assertRaises(ValueError):
            main.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
