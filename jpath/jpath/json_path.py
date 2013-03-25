# -*- coding: utf-8 -*-

# XPATH PARA XML - http://www.w3schools.com/xpath/xpath_syntax.asp

import networkx
import sys
import json


def indent(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def all_keys(data):
    '''
      pt_BR: Retorna todas as chaves do documento
      en_US: Return all keys from document
    '''
    keys = data.keys()
    result = []
    result = extraxt_keys(data, keys, result)
    return result

def all_values(data):
    '''
      pt_BR: Retorna todos os valores do documento
      en_US: Return all values from document
    '''
    keys = data.keys()
    result = []
    result = extraxt_values(data, keys, result)
    return result

def all_values_for_key(key, data):
    pass

def query_by_keys(keys, data=None):
    '''
      pt_BR: Retorna os valores de acordo com o caminho ( ie.: cliente$nome$ )
      en_US: Returns values ​​in accordance with path ( ie.: cliente$nome$ )
    '''
    pass

def query_list_by_keys(keys, data=None):
    pass

def extraxt_keys(data, key, result, parent=None):
    print 'parent: ' + str(parent)
    print 'key: ' + str(key)
    for k in key:
	if parent != None:
	  if isinstance(key, list):
	    #aqui ta fd.....
	    result += [parent + ':' + [x for x in key]]
	  else:
	    result += [parent + ':' + key]
	else:
	  result += key
        v = data[k]

        print 'k: ' + str(k)
        print 'v: ' + str(v)
        print 'result: ' + str(result)

	if parent != None:
	  actual_parent = parent + ':' + k;
	else:
	  actual_parent = k;

        if isinstance(v, dict):
            extraxt_keys(v, v.keys(), result, actual_parent)
        elif isinstance(v, list):
            for l in v:
                if isinstance(l, dict):
                    extraxt_keys(l, l.keys(), result, actual_parent)
    return result

def extraxt_values(data, keys, result):
    for k in keys:
        v = data[k]
        if isinstance(v, dict):
            extraxt_values(v, v.keys(), result)
        elif isinstance(v, list):
            for l in v:
                if isinstance(l, dict):
                    extraxt_values(l, l.keys(), result)
        else:
            result.append(v)
    return result
