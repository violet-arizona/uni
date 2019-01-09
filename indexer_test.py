"""This module contains a set of tests for 'indexer.py' module"""
import shutil, tempfile
from os import path
import unittest
import indexer
import shelve


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.temp_directory = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.temp_directory)

    def create_textFile(self, directory, text):
        # Create a file in the temporary directory and write something to it
        f = open(path.join(directory, 'test.txt'), 'w', encoding='utf-8')
        f.write(text)
        f.close()
        
    def test_simple_sentence(self):
        TestDatabase().create_textFile(self.temp_directory, 'The owls are not what they seem.')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 7)
        test_dict = {'the': [0], 'owls': [4], 'are': [9], 'not': [13],'what': [17], 'they': [22], 'seem': [27]}
        self.assertEqual(result, test_dict)
        result.close()

    def test_multicategory_string(self):
        TestDatabase().create_textFile(self.temp_directory, '-Мама, помой раму! - сказала дочь 8, мама 589 64')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 8)
        test_dict = {'мама': [1, 37], 'помой': [7], 'раму': [13], 'сказала': [21], 'дочь': [29], '8': [34], '589': [42], '64': [46]}
        self.assertEqual(result, test_dict)
        result.close()

    def test_punctuation_string(self):
        TestDatabase().create_textFile(self.temp_directory, '- , ! ...')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 0)
        result.close()

    def test_empty_string(self):
        TestDatabase().create_textFile(self.temp_directory, '')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 0)
        result.close()
        
if __name__ == '__main__':
    unittest.main()
