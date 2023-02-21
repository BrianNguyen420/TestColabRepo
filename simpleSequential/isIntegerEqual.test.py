import unittest
from isIntegerEqual import isIntegerEqual

class TestIsIntegerEqualFunction(unittest.TestCase):
    def test_isIntergerEqualCase1(self):
        self.assertEqual(isIntegerEqual(2, 2), True, "Error: isIntergerEqual result is incorrect.")

    def test_isIntergerEqualCase2(self):
        self.assertEqual(isIntegerEqual(1, 3), False, "Error: isIntergerEqual result is incorrect.")

if __name__ == "__main__":
    unittest.main()