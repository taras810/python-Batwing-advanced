import unittest
from functions_to_test import Calculator


class TestForCalculator(unittest.TestCase):
    def setUp(self):
        self.classTest = Calculator(9, 3)
        self.classTest2 = Calculator(9, 0)
        self.classTest3 = Calculator(-1, 4)

    def test_add(self):
        self.assertEqual(self.classTest.add(), 12)
        self.assertEqual(self.classTest2.add(), 9)
        self.assertEqual(self.classTest3.add(), 3)

    def test_subtract(self):
        self.assertEqual(self.classTest.subtract(), 6)
        self.assertEqual(self.classTest2.subtract(), 9)
        self.assertEqual(self.classTest3.subtract(), -5)

    def test_multiply(self):
        self.assertEqual(self.classTest.multiply(), 27)
        self.assertEqual(self.classTest2.multiply(), 0)
        self.assertEqual(self.classTest3.multiply(), -4)

    def test_divide(self):
        self.assertEqual(self.classTest.divide(), 3)
        with self.assertRaises(ValueError):
            self.classTest2.divide()
        self.assertEqual(self.classTest3.divide(), -0.25)


if __name__ == '__main__':
    unittest.main()
