# -*- coding: utf-8 -*-

# XPATH PARA XML - http://www.w3schools.com/xpath/xpath_syntax.asp

import jpath.json_path as jpath

def all_values(data):
    '''
      pt_BR: Retorna todos os valores do documento
      en_US: Return all values from document
    '''
    keys = data.keys()
    result = []
    result = jpath.extraxt_values(data, keys, result)
    print 'result: ' + str(result)
    return result
