"""This module contains a set of tests for 'fullTok.py' module"""
import unittest
import fullTok

class TestTokenizationMethods(unittest.TestCase):

    def test_not_str(self):
        with self.assertRaises(TypeError):
            fullTok.Tokenizer().tokenizeCat([1, 2, 3])

    def test_type_of_symbol_digit(self):
        result = fullTok.Tokenizer().checkCategory('1')
        self.assertEqual(result, "digit")

    def test_type_of_symbol_alpha(self):
        result = fullTok.Tokenizer().checkCategory('Я')
        self.assertEqual(result, "word")

    def test_type_of_symbol_space(self):
        result = fullTok.Tokenizer().checkCategory(' ')
        self.assertEqual(result, "space")

    def test_type_of_symbol_punct(self):
        result = fullTok.Tokenizer().checkCategory(',')
        self.assertEqual(result, "punctuation")
        
    def test_type_of_symbol_other(self):
        result = fullTok.Tokenizer().checkCategory('=')
        self.assertEqual(result, "other")

    def test_multicategory_string(self):
        result = fullTok.Tokenizer().tokenizeCat("Мама дома!")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].tok,"мама")
        self.assertEqual(result[0].pos, 0)
        self.assertEqual(result[0].cat, "word")
        self.assertEqual(result[1].tok," ")
        self.assertEqual(result[1].pos, 4)
        self.assertEqual(result[1].cat, "space")
        self.assertEqual(result[2].tok,"дома")
        self.assertEqual(result[2].pos, 5)
        self.assertEqual(result[2].cat, "word")
        self.assertEqual(result[3].tok,"!")
        self.assertEqual(result[3].pos, 9)
        self.assertEqual(result[3].cat, "punctuation")

    def test_multipunct_str(self):
        result = fullTok.Tokenizer().tokenizeCat("Мама, помой раму!!! А я мыла пол, глядя на кота...эх")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 24)
        self.assertEqual(result[6].tok,"!!!")
        self.assertEqual(result[6].pos, 16)
        self.assertEqual(result[6].cat, "punctuation")
        self.assertEqual(result[22].tok,"...")
        self.assertEqual(result[22].pos, 47)
        self.assertEqual(result[22].cat, "punctuation")

    def test_empty_str(self):
        result = fullTok.Tokenizer().tokenizeCat("")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_one_symbol_str(self):
        result = fullTok.Tokenizer().tokenizeCat("5")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
