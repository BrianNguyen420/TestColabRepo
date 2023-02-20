import unittest
from multiply import multiply

class TestMultiplyFuction(unittest.TestCase):
    def test_multiplyTwoNumberCase1(self):
        self.assertEqual(multiply(2, 3), 6, "Error: multiply result is incorrect.")

    def test_multiplyTwoNumberCase2(self):
        self.assertEqual(multiply(3, -3), -9, "Error: multiply result is incorrect.")
        
    def test_multiplyTwoNumberCase3(self):
        self.assertEqual(multiply(3, -1), -3, "Error: multiply result is incorrect.")

if __name__ == "__main__":
    unittest.main()
