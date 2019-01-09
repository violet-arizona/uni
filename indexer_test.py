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

    def create_textFile(self, directory, name, text):
        # Create a file in the temporary directory and write something to it
        f = open(path.join(directory, name), 'w', encoding='utf-8')
        f.write(text)
        f.close()
        
    def test_simple_sentence(self):
        TestDatabase().create_textFile(self.temp_directory, 'test.txt', 'The owls are not what they seem.')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 7)
        test_dict = {'the': {'test.txt':[0]}, 'owls': {'test.txt':[4]}, 'are': {'test.txt':[9]}, 'not': {'test.txt':[13]},
                     'what': {'test.txt':[17]}, 'they': {'test.txt':[22]}, 'seem': {'test.txt':[27]}}
        self.assertEqual(result, test_dict)
        result.close()

    def test_multicategory_string(self):
        TestDatabase().create_textFile(self.temp_directory, 'test.txt', '-Мама, помой раму! - сказала дочь 8, мама 589 64')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 8)
        test_dict = {'мама': {'test.txt':[1, 37]}, 'помой': {'test.txt':[7]}, 'раму': {'test.txt':[13]}, 'сказала': {'test.txt':[21]},
                     'дочь': {'test.txt':[29]}, '8': {'test.txt':[34]}, '589': {'test.txt':[42]}, '64': {'test.txt':[46]}}
        self.assertEqual(result, test_dict)
        result.close()

    def test_several_files(self):
        TestDatabase().create_textFile(self.temp_directory, 'one.txt', '-Мама, помой раму! - сказала дочь.')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'one.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 5)
        TestDatabase().create_textFile(self.temp_directory, 'two.txt', 'Мама, ты помыла раму?')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'two.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 7)
        test_dict = {'мама': {'one.txt': [1], 'two.txt': [0]}, 'помой': {'one.txt': [7]}, 'раму': {'one.txt': [13], 'two.txt': [16]},
                     'сказала': {'one.txt': [21]}, 'дочь': {'one.txt': [29]}, 'ты': {'two.txt': [6]}, 'помыла': {'two.txt': [9]}}
        self.assertEqual(result, test_dict)
        result.close()

    def test_punctuation_string(self):
        TestDatabase().create_textFile(self.temp_directory, 'test.txt', '- , ! ...')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 0)
        result.close()

    def test_empty_string(self):
        TestDatabase().create_textFile(self.temp_directory, 'test.txt', '')
        indexer.Database().toDB(path.join(self.temp_directory, 'testDB'), path.join(self.temp_directory, 'test.txt'))
        result = shelve.open(path.join(self.temp_directory, 'testDB'), 'r')
        self.assertEqual(len(result), 0)
        result.close()
        
if __name__ == '__main__':
    unittest.main()
