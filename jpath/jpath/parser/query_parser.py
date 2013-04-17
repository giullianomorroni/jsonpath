# -*- coding: utf-8 -*-
'''
Created on 22/03/2013

@author: giulliano
'''

import jpath.json_path as jpath
import jpath.extractor.values_extractor as values_ex
import jpath.extractor.keys_extractor as keys_ex
import jpath.extractor.graph_extractor as graph_ex
import json
#import ast

class QueryParser(object):
    '''
    pt_BR: Realiza a leitura da consulta para determinar qual metodo executar
    en_US: 
    '''

    def parse(self, query, data):
        result = []
        url= None;
        print 'data: ' + data
        print 'query: ' + query
        data = json.loads(str(data))

        if query.lower() == '_lv':
            print 'method: all_values'
            result = values_ex.all_values(data)
            
        elif query.lower() == '_sv':
            print 'method: all_values'
            result = set(values_ex.all_values(data))
                
        elif query.lower() == '_lk':
            print 'method: all_keys'
            result = sorted(keys_ex.all_keys(data))

        elif query.lower() == '_sk':
            print 'method: all_keys'
            result = sorted(set(keys_ex.all_keys(data)))

        elif query.lower() == '_tg':
            print 'method: draw_graph'
            result = graph_ex.draw_graph(data)
            #print 'method: not yet implemented'
            #result = ['not yet implemented']

        elif query.__contains__(':'):
            print 'method: query_by_keys'
            r, url = graph_ex.query_by_keys(query, data)
            for x in r:
                result.append(x)
        else:
            print 'method: all_values_for_key'
            result = jpath.all_values_for_key(query, data)

        return result, url