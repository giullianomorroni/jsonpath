# -*- coding: utf-8 -*-

def all_values(data):
    '''
      pt_BR: Retorna todos os valores do documento
      en_US: Return all values from document
    '''
    keys = data.keys()
    result = []
    result = extraxt_values(data, keys, result)
    print 'result: ' + str(result)
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

