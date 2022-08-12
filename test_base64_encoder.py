import unittest
from base64_text_encoder import encode_base64

class test_base64_encoder(unittest.TestCase):

    def test_capital_letters(self):
        self.assertEqual(encode_base64("ABC") , "QUJD", "Should be QUJD")

    def test_small_letters(self):
        self.assertEqual(encode_base64("abc") , "YWJj", "Should be YWJj")

    def test_numeric(self):
        self.assertEqual(encode_base64("102030") , "MTAyMDMw", "Should be MTAyMDMw")

    def test_anything(self):
        self.assertEqual(encode_base64("amin1213ABC") , "YW1pbjEyMTNBQkM=", "Should be YW1pbjEyMTNBQkM=")
    
    def test_longText(self):
        self.assertEqual(
            encode_base64("0012:Change your body, change your life!"),
             "MDAxMjpDaGFuZ2UgeW91ciBib2R5LCBjaGFuZ2UgeW91ciBsaWZlIQ==",
             "Should be MDAxMjpDaGFuZ2UgeW91ciBib2R5LCBjaGFuZ2UgeW91ciBsaWZlIQ==")

if __name__ == "__main__":
    unittest.main()
