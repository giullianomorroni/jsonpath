# -*- coding: utf-8 -*-
'''
Created on 22/03/2013

@author: giulliano
'''

import json_path as jpath 

class QueryParser(object):
    '''
    pt_BR: Realiza a leitura da consulta para determinar qual metodo executar
    en_US: 
    '''

    def parse(self, query, data):
        result = []
        print 'data: ' + str(data)
        print 'query: ' + str(query)

        if query.lower() == '_lv':
            print 'method: all_values'
            result = jpath.all_values(data)
            
        elif query.lower() == '_lk':
            print 'method: all_keys'
            result = jpath.all_keys(data)
            
        elif query.lower() == '_tg':
            print 'method: not yet implemented'
            result = ['not yet implemented']
                    
        elif query.__contains__('$'):
            keys = query.split('$')
            if len(keys) == 2:
                print 'method: all_values_for_key'
                result = jpath.all_values_for_key(query, data)
            else:
                print 'method: query_by_keys'
                result = jpath.query_by_keys(query, data)

        else:
            print 'method: all_values_for_key'
            result = jpath.all_values_for_key(query, data)

        print 'result: ' + str(result)
        return result