# -*- coding: utf-8 -*-

def all_keys(data):
    '''
      pt_BR: Retorna todas as chaves do documento
      en_US: Return all keys from document
    '''
    result = []
    if isinstance(data, list):
        for d in data:
            keys = d.keys()
            extraxt_keys(d, keys, result)
            keys = None
    else:
        keys = data.keys()
        extraxt_keys(data, keys, result)
    return result

def extraxt_keys(data, key, result, parent=None):
    for k in key:
        if parent != None:
            if isinstance(key, list):
                for x in key:
                    result += [parent + ':' + x + ':']
            else:
                result += [parent + ':' + key + ':']
        else:
            result += [k + ':']

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