import unittest
import myToken

class TestStringMethods(unittest.TestCase):

    def test_simple_string(self):
        result = myToken.Tokenizer().tokenize("Мама мыла раму.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        #self.assertEqual(repr(result[2]),"10 раму;")

    def test_str_ends_with_letter(self):
        result = myToken.Tokenizer().tokenize("Мама мыла раму")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        #example = __str__(result[2])
        #self.assertEqual(example,"10 раму;")

    def test_empty_str(self):
        result = myToken.Tokenizer().tokenize("")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_not_str(self):
        result = myToken.Tokenizer().tokenize([1, 2, 3])
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Argument must be a string!")

    def test_one_letter_str(self):
        result = myToken.Tokenizer().tokenize("A")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_one_symbol_str(self):
        result = myToken.Tokenizer().tokenize("5")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_multipunct_str(self):
        result = myToken.Tokenizer().tokenize("Мама, помой раму!!! А я мыла пол, глядя на кота...эх")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 11)

    def test_str_starts_with_punct(self):
        result = myToken.Tokenizer().tokenize("-Мама, помой раму! - сказала дочь.")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        #self.assertEqual(repr(result[0]),"1 Мама;")
        

if __name__ == '__main__':
    unittest.main()
