'''
Created on 22/03/2013

@author: giulliano
'''
import unittest
import jpath.extractor.keys_extractor as keys_extractor
import jpath.extractor.values_extractor as values_extractor
import jpath.extractor.graph_extractor as graph_extractor

class Test(unittest.TestCase):

    def testCase1_AllKeys(self):
        data = {"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }
        keys = keys_extractor.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore:'))
        self.assertTrue(keys.__contains__('bookstore:book:'))
        self.assertTrue(keys.__contains__('bookstore:book:name:'))

    def testCase2_AllKeys(self):
        data = {"bookstore": {"book":{"name":"jpath"}} }
        keys = keys_extractor.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore:'))
        self.assertTrue(keys.__contains__('bookstore:book:'))
        self.assertTrue(keys.__contains__('bookstore:book:name:'))

    def testCase3_AllKeys(self):
        data = {"bookstore": ["jpath"] }
        keys = keys_extractor.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore:'))

    def testCase4_AllKeys(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        keys = keys_extractor.all_keys(data)
        self.assertTrue(keys.__contains__('bookstore:'))
        self.assertTrue(keys.__contains__('bookstore:books:'))
        self.assertTrue(keys.__contains__('bookstore:books:name:'))
        self.assertTrue(keys.__contains__('bookstore:books:authors:'))
        self.assertTrue(keys.__contains__('bookstore:books:authors:author:'))
        
    def testCase1_AllValues(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = values_extractor.all_values(data)
        print values
        self.assertTrue(values.__contains__('jpath'))
        self.assertTrue(values.__contains__('joe'))
        self.assertTrue(values.__contains__('jquery'))
        
    def testCase1_QueryByKeys(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = graph_extractor.query_by_keys('bookstore:books', data);
        values = values.replace('\'', '"')
        print values
        self.assertTrue(values.__contains__('[{"name": "jpath", "authors": [{"author": "joe"}]}, {"name": "jquery"}]'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()