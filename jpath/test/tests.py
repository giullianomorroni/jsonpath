'''
Created on 22/03/2013

@author: giulliano
'''
import unittest
import jpath.json_path as jpath

class Test(unittest.TestCase):

    def testAllKeys(self):
        data = '{"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }'
        values = jpath.all_keys(data)
        self.assertTrue(values.__contains__('bookstore'))
        self.assertTrue(values.__contains__('book'))
        self.assertTrue(values.__contains__('name'))
        self.assertEqual(len(values), 3)

    def testAllValues(self):
        data = '{"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }'
        values = jpath.all_values(data)
        self.assertTrue(values.__contains__('jquery'))
        self.assertTrue(values.__contains__('jpath'))

    def testCase1_QueryValuesWithOneKey(self):
        data = '{"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }'
        key = 'name'
        values = jpath.all_values_for_key(key, data);
        self.assertTrue(values.__contains__('jquery'))
        self.assertTrue(values.__contains__('jpath'))

    def testCase2_QueryValuesWithOneKey(self):
        data = '{"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }'
        key = 'name'
        values = jpath.all_values_for_key(key, data);
        self.assertTrue(values.__contains__('jquery'))
        self.assertTrue(values.__contains__('jpath'))

    def testCase1_QueryValuesByPathWithOneKey(self):
        data = '{"bookstore": [ {"book":{"name":"jpath"}}, {"book":{"name":"jquery"}} ] }'
        key = '$bookstore'
        values = jpath.query_by_keys(key, data)
        self.assertTrue(values[0].__contains__('jpath'))
        self.assertTrue(values[1].__contains__('jquery'))
        self.assertEqual(len(values), 2)

    def testCase2_QueryValuesByPathWithOneKey(self):
        data = '{"bookstore": [ {"book":{"name":"jpath", "id":1}}, {"book":{"name":"jquery", "id":2}} ] }'
        key = '$bookstore'
        values = jpath.query_by_keys(key, data)
        self.assertTrue(values[0].__contains__('jpath'))
        self.assertTrue(values[1].__contains__('1'))
        self.assertTrue(values[2].__contains__('jquery'))
        self.assertTrue(values[3].__contains__('2'))
        self.assertEqual(len(values), 4)

    def testCase3_QueryValuesWrongPath(self):
        data = '{"bookstore": [ {"book":{"name":"jpath", "id":1}}, {"book":{"name":"jquery", "id":2}} ] }'
        key = '$book'
        values = jpath.query_by_keys(key, data)
        self.assertEqual(len(values), 0)

    def testCase4_QueryValuesByPathWithTwoKeys(self):
        data = '{ "results":["id":"1", "id":"2"] }'
        key = '$results$id'
        values = jpath.query_by_keys(key, data)
        self.assertTrue(values[0].__contains__('1'))
        self.assertTrue(values[1].__contains__('2'))
        self.assertEqual(len(values), 2)

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()