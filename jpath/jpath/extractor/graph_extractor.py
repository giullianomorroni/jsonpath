# -*- coding: utf-8 -*-

import networkx

def make_graph(data):
    '''
      pt_BR: Retorna um grafico do documento
      en_US: Return a graph from document
    '''
    keys = data.keys()
    result = []
    graphic = create_graph(data, keys, result)
    print 'graphic: ' + str(graphic)
    return graphic

grafico = networkx.Graph()
def create_graph(data, key, result, parent = None):
    for k in key:
        value = data[k]

        if parent != None:
            grafico.add_node(str(k), data={ 'value':str(value), 'parent':str(parent) })
            grafico.add_edge(parent, str(k))
        else:
            grafico.add_node(str(k), data={ 'value':str(value), 'parent':str(parent) })    

        print 'nodes: ' + str(grafico.nodes())
        print 'edges: ' + str(grafico.edges())

        if isinstance(value, dict):
            create_graph(value, value.keys(), result, k)
        elif isinstance(value, list):
            for l in value:
                if isinstance(l, dict):
                    create_graph(l, l.keys(), result, k)
    return grafico
