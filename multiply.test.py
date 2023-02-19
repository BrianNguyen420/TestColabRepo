import unittest
from multiply import multiply

class TestMulFuction(unittest.TestCase):
    def test_mulTwoNumberCase1(self):
        self.assertEqual(multiply(2, 3), 6, "Error: multiply result is incorrect.")

    def test_mulTwoNumberCase2(self):
        self.assertEqual(multiply(3, -3), -9, "Error: multiply result is incorrect.")
        
    def test_mulTwoNumberCase3(self):
        self.assertEqual(multiply(3, -1), -3, "Error: multiply result is incorrect.")

if __name__ == "__main__":
    unittest.main()