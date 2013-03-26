# -*- coding: utf-8 -*-

# XPATH PARA XML - http://www.w3schools.com/xpath/xpath_syntax.asp

import networkx
import json

def indent(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def all_values_for_key(key, data):
    pass

def query_by_keys(keys, graph):
    '''
      pt_BR: Retorna os valores de acordo com o caminho ( ie.: cliente$nome$ )
      en_US: Returns values ​​in accordance with path ( ie.: cliente$nome$ )
    '''
    all_keys = keys.split(':')
    k = all_keys.pop(0)
    if k == '': k = all_keys.pop(0)

    if not graph.node.__contains__(k):
        return []

    node = graph.node[k]
    #continua daqui
        

def query_list_by_keys(keys, data=None):
    pass

def extraxt_keys(data, key, result, parent=None):
    for k in key:
        if parent != None:
            if isinstance(key, list):
                for x in key:
                    result += [parent + ':' + x + ':']
            else:
                result += [parent + ':' + key + ':']
        else:
            result += [key[0] + ':']
        v = data[k]

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

def extraxt_values(data, key, result, parent = None):
    for k in key:
        value = data[k]

        if isinstance(value, dict):
            extraxt_values(value, value.keys(), result, k)
        elif isinstance(value, list):
            for l in value:
                if isinstance(l, dict):
                    extraxt_values(l, l.keys(), result, k)
        else:
            result.append(value)
    return result

