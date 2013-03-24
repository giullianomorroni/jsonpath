'''
Created on 22/03/2013

@author: giulliano
'''
import unittest
import jpath.json_path as jpath

class Test(unittest.TestCase):

    def testCase1_AllKeys(self):
        data = {"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }
        keys = jpath.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore'))
        self.assertTrue(keys.__contains__('book'))
        self.assertTrue(keys.__contains__('name'))

    def testCase2_AllKeys(self):
        data = {"bookstore": {"book":{"name":"jpath"}} }
        keys = jpath.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore'))
        self.assertTrue(keys.__contains__('book'))
        self.assertTrue(keys.__contains__('name'))

    def testCase3_AllKeys(self):
        data = {"bookstore": ["jpath"] }
        keys = jpath.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore'))

    def testCase4_AllKeys(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        keys = jpath.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore'))
        self.assertTrue(keys.__contains__('books'))
        self.assertTrue(keys.__contains__('name'))
        self.assertTrue(keys.__contains__('authors'))
        self.assertTrue(keys.__contains__('author'))
        
    def testCase1_AllValues(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = jpath.all_values(data)
        print values
        self.assertTrue(values.__contains__('jpath'))
        self.assertTrue(values.__contains__('joe'))
        self.assertTrue(values.__contains__('jquery'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()