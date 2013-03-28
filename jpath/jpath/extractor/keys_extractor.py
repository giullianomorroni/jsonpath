# -*- coding: utf-8 -*-


def all_keys(data):
    '''
      pt_BR: Retorna todas as chaves do documento
      en_US: Return all keys from document
    '''
    keys = data.keys()
    result = []
    result = extraxt_keys(data, keys, result)
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