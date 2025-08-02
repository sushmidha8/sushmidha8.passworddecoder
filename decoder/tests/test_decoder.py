import unittest
from ..decoder.decoder import PasswordDecoder

class TestPasswordDecoder(unittest.TestCase):
    def setUp(self):
        self.decoder = PasswordDecoder()
    
    def test_valid_passwords(self):
        self.assertEqual(self.decoder.decode("104 101 108 108 111"), "hello")
        self.assertEqual(self.decoder.decode("97 98 99"), "cba")
    
    def test_invalid_passwords(self):
        self.assertIsNone(self.decoder.decode("not_a_number"))
        self.assertIsNone(self.decoder.decode("999999"))  # Invalid ASCII
    
    def test_stats(self):
        self.decoder.decode("104 101 108 108 111")  # ✅ Valid
        self.decoder.decode("invalid")              # ❌ Invalid
        stats = self.decoder.get_stats()
        self.assertEqual(stats["total_attempts"], 2)
        self.assertEqual(stats["success_rate"], "50.0%")

if __name__ == "__main__":
    unittest.main()