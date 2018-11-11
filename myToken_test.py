"""This module contains a set of tests for 'myToken.py' module"""
import unittest
import myToken

class TestStringMethods(unittest.TestCase):

    def test_simple_string(self):
        result = myToken.Tokenizer().tokenize("Мама мыла раму.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].word,"Мама")
        self.assertEqual(result[0].pos, 0)
        self.assertEqual(result[1].word,"мыла")
        self.assertEqual(result[1].pos, 5)
        self.assertEqual(result[2].word,"раму")
        self.assertEqual(result[2].pos, 10)

    def test_str_ends_with_letter(self):
        result = myToken.Tokenizer().tokenize("Мама мыла раму")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[2].word,"раму")
        self.assertEqual(result[2].pos, 10)

    def test_empty_str(self):
        result = myToken.Tokenizer().tokenize("")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_not_str(self):
        with self.assertRaises(TypeError):
            myToken.Tokenizer().tokenize([1, 2, 3])

    def test_one_letter_str(self):
        result = myToken.Tokenizer().tokenize("A")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].word, "A")
        self.assertEqual(result[0].pos, 0)

    def test_one_symbol_str(self):
        result = myToken.Tokenizer().tokenize("5")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_multipunct_str(self):
        result = myToken.Tokenizer().tokenize("Мама, помой раму!!! А я мыла пол, глядя на кота...эх")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 11)
        self.assertEqual(result[1].word, "помой")
        self.assertEqual(result[1].pos, 6)
        self.assertEqual(result[2].word, "раму")
        self.assertEqual(result[2].pos, 12)
        self.assertEqual(result[3].word, "А")
        self.assertEqual(result[3].pos, 20)
        self.assertEqual(result[9].word, "кота")
        self.assertEqual(result[9].pos, 43)
        self.assertEqual(result[10].word, "эх")
        self.assertEqual(result[10].pos, 50)

    def test_str_starts_with_punct(self):
        result = myToken.Tokenizer().tokenize("-Мама, помой раму! - сказала дочь.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].word, "Мама")
        self.assertEqual(result[0].pos, 1)
        

if __name__ == '__main__':
    unittest.main()
