import unittest


def uppercase(text):
    return text.upper()


class TestUpper(unittest.TestCase):
    def test_one_word(self):
        text = "hello"
        result = uppercase(text)
        self.assertEqual(result, "HELLO")
        self.assertNotEqual(result, "Hello")

    def test_mul_word(self):
        text = "hello world"
        result = uppercase(text)
        self.assertEqual(result, "HELLO WORLD")


