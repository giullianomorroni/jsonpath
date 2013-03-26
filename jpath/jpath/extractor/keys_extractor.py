# -*- coding: utf-8 -*-

import jpath.json_path as jpath

def all_keys(data):
    '''
      pt_BR: Retorna todas as chaves do documento
      en_US: Return all keys from document
    '''
    keys = data.keys()
    result = []
    result = jpath.extraxt_keys(data, keys, result)
    print 'result: ' + str(result)
    return result
