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


    def testCase5_AllKeys(self):
        data = {"titulo": "JSON x XML","resumo": "o duelo de dois modelos de representa","ano": 2012,"genero": ["aventura", "romance"]}
        keys = keys_extractor.all_keys(data)
        self.assertTrue(keys.__contains__('titulo:'))
        self.assertTrue(keys.__contains__('resumo:'))
        self.assertTrue(keys.__contains__('ano:'))
        self.assertTrue(keys.__contains__('genero:'))

        
    def testCase1_AllValues(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = values_extractor.all_values(data)
        self.assertTrue(values.__contains__('jpath'))
        self.assertTrue(values.__contains__('joe'))
        self.assertTrue(values.__contains__('jquery'))

    def testCase2_AllValues(self):
        data = {"titulo": "JSON x XML","resumo": "o duelo de dois modelos","ano": 2012,"genero": ["aventura", "romance"]}
        values = values_extractor.all_values(data)
        self.assertTrue(values.__contains__('JSON x XML'))
        self.assertTrue(values.__contains__('o duelo de dois modelos'))
        self.assertTrue(values.__contains__(2012))
        self.assertTrue(values.__contains__('aventura'))
        self.assertTrue(values.__contains__('romance'))

    def testCase1_QueryByKeys(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = graph_extractor.query_by_keys('bookstore:books', data);
        st_values = str(values)
        st_values = st_values.replace('\'', '"')
        self.assertTrue(st_values.__contains__('[{"name": "jpath", "authors": [{"author": "joe"}]}, {"name": "jquery"}]'))

    def testCase2_QueryByKeys(self):
        data = {"bookstore": [ {"books": [{"name":"jpath", "authors": [ {"author": "joe"} ]}, {"name":"jquery"}] }] }
        values = graph_extractor.query_by_keys('bookstore:books:name', data);
        print values
        self.assertTrue(values.__contains__('jquery'))
        self.assertTrue(values.__contains__('jpath'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()