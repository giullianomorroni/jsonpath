# -*- coding: utf-8 -*-

#XPATH PARA XML - http://www.w3schools.com/xpath/xpath_syntax.asp

import re
import json
import sys

#data_example = '{"id":1, "name":"Giulliano", "age":30, "parentes": [{"id":2, "name":"Joyce", "age":28, "parentes": [{"id":3, "name":"Soraya", "age":50}]}]}'

data_example = ''
data_example += '[{"id":1, "name":"Giulliano", "age":30, "parentes": [{"id":2, "name":"Joyce", "age":28}]},'
data_example += '{"id":1, "name":"Yuri", "age":25, "parentes": [{"id":2, "name":"Eduardo", "age":50}]},'
data_example += '{"id":1, "name":"Soraya", "age":30, "parentes": [{"id":2, "name":"Joyce", "age":28}]}]'

def all_keys():
  '''
    pt_BR: Retorna todas as cahves do documento
    en_US: Return all keys from document
  '''
  #remove aspas duplas e simples
  #remove espaçoes em branco
  data = data_example.replace('"', '').replace(' ', '') 
  data = eval(str(data_example))
  keys = []
  if isinstance(data, list):
    for d in data:
      data = dict(d)
      for k in data.keys():
	keys.append(k)
      data = None;
  else:
    data = dict(data)
    keys = data.keys()
  return set(keys)

def all_values():
  '''
    pt_BR: Retorna todos os valores do documento
    en_US: Return all values from document
  '''
  data = data_example.replace('"', '').replace(' ', '') #remove aspas duplas #remove espaçoes em branco
  rgx_values = re.compile(':\w+')
  _values = rgx_values.findall(data)
  result = []
  for i in _values:
    aux = i.replace(':','')
    result.append(aux)
  return result

def all_values_for_key(key):
  data = data_example.replace('"', '').replace(' ', '') #remove aspas duplas #remove espaçoes em branco
  rgx_id_value = re.compile(key + ':\w+')
  rgx_values = re.compile(':\w+')

  _id_values = rgx_id_value.findall(data)
  result = []
  for i in _id_values:
    v = rgx_values.findall(i)
    if len(v) > 0:
      aux = v[0].replace(':','')
      result.append(aux)
  return result


def query_by_keys(keys, data=None):
  '''
    pt_BR: Retorna os valores de acordo com o caminho ( ie.: cliente$nome$ )
    en_US: Returns values ​​in accordance with path ( ie.: cliente$nome$ )
  '''
  if data == None:
    data = data_example
  if str(data)[0] == '[':
    return query_list_by_keys(keys, data)

  try:
    keys = keys.split('$')
    json_data = eval(str(data))
    _value = json_data
    while(len(keys)):
      key = keys.pop(0)
      if key == '': continue

      _value = _value[key]
      if isinstance(_value, list):
	_value = _value[0]

    rgx_values = re.compile(':\w+')
    aux = str(_value)
    aux = aux.replace(' ','').replace('\'','').replace('"','')
    _values = rgx_values.findall(aux)
    result = []
    for r in _values:
      result.append(r.replace(':',''))
    return result
  except (TypeError, KeyError,NameError):
    print sys.exc_info()[0]
    return []


def query_list_by_keys(keys, data=None):
  if data == None:
    data = data_example
  json_data = eval(data)
  _values = []
  _keys = keys
  for j in json_data:
    _aux = query_by_keys(_keys, j)
    _keys = keys
    if (len(_aux) > 0):
      _values.append(_aux)
  return _values
