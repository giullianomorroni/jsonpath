# -*- coding: utf-8 -*-

# XPATH PARA XML - http://www.w3schools.com/xpath/xpath_syntax.asp

import re
import sys

def all_keys(data):
    '''
      pt_BR: Retorna todas as chaves do documento
      en_US: Return all keys from document
    '''
    data = data.replace('"', '').replace(' ', '')
    rgx_values = re.compile('\w+:')
    _values = rgx_values.findall(data)
    result = []
    for i in _values:
        aux = i.replace(':', '')
        result.append(aux)
    return set(result)

def all_values(data):
    '''
      pt_BR: Retorna todos os valores do documento
      en_US: Return all values from document
    '''
    data = data.replace('"', '').replace(' ', '')
    rgx_values = re.compile(':\w+')
    _values = rgx_values.findall(data)
    result = []
    for i in _values:
        aux = i.replace(':', '')
        result.append(aux)
    return result

def all_values_for_key(key, data):
    data = data.replace('"', '').replace(' ', '')
    rgx_id_value = re.compile(key + ':\w+')
    rgx_values = re.compile(':\w+')

    _id_values = rgx_id_value.findall(data)
    result = []
    for i in _id_values:
        v = rgx_values.findall(i)
        if len(v) > 0:
            aux = v[0].replace(':', '')
            result.append(aux)
    return result


def query_by_keys(keys, data=None):
    '''
      pt_BR: Retorna os valores de acordo com o caminho ( ie.: cliente$nome$ )
      en_US: Returns values ​​in accordance with path ( ie.: cliente$nome$ )
    '''
    if str(data)[0] == '[':
        print 'changing to query_list_by_keys'
        return query_list_by_keys(keys, data)

    try:
        keys = keys.split('$')
        print 'data: ' + str(data)
        json_data = eval(str(data))
        print 'json_data: ' + str(json_data)
        _value = json_data
        dicts = []

        key = keys.pop(0)
        # Se a primeira chave for vazia, pega a próxima
        # Isto ocorre dependendo do uso do $ para uma palavra
        if key == '':
            key = keys.pop(0)

        print 'key: ' + key
        _value = _value[key]
        if isinstance(_value, list):
            for v in _value:
                dicts.append(v)
        else:
            dicts.append(_value)

        print 'dicts: ' + str(dicts)
    
        new_dicts = []
        ttl_keys = len(keys)
        if ttl_keys == 0:
            new_dicts = dicts;

        while ttl_keys != 0:
            ttl_keys = ttl_keys-1
            new_dicts = []
            for d in dicts:
                key = keys.pop(0)
                print 'key: ' + key
                if isinstance(d, list):
                    for v in d:
                        new_dicts.append(v[key])
                else:
                    new_dicts.append(d[key])
                print 'new_dicts: ' + str(new_dicts)

                if isinstance(dicts, dict):
                    dicts.clear()
                dicts = new_dicts

        rgx_values = re.compile(':\w+')
        _value = str(new_dicts)
        aux = str(_value)
        aux = aux.replace(' ', '').replace('\'', '').replace('"', '')
        _values = rgx_values.findall(aux)
        result = []
        for r in _values:
            result.append(r.replace(':', ''))
        return result
    except (TypeError, KeyError, NameError):
        print sys.exc_info()
        return []


def query_list_by_keys(keys, data=None):
    json_data = eval(data)
    _values = []
    _keys = keys
    for j in json_data:
        _aux = query_by_keys(_keys, j)
        _keys = keys
        if (len(_aux) > 0):
            _values.append(_aux)
    return _values
