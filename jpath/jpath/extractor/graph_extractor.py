# -*- coding: utf-8 -*-

import networkx
import matplotlib.pyplot as plt

from jpath.graph.GraphSearch import graph_search

G = networkx.Graph()

def query_by_keys(keys, data):
    '''
      pt_BR: Retorna os valores de acordo com o caminho ( ie.: cliente$nome$ )
      en_US: Returns values ​​in accordance with path ( ie.: cliente$nome$ )
    '''

    graph = make_graph(data)

    gs = graph_search()
    all_keys = keys.split(':')
    k = all_keys.pop(0)
    if k == '': k = all_keys.pop(0)

    node = gs.search_node(k, graph);
    if node == None:
        return []

    while(True):
        k2 = all_keys.pop(0)
        if k2 == '': break 
        edge = gs.search_edge(k, k2, graph);
        if edge == None:
            print 'Não existe ponte entre %s e %s' % (k,k2)
            return []
        node = gs.search_node(k2, graph);
        k = k2
        if len(all_keys) == 0: break
    G.clear()
    graph.clear()
    return node['data']['value']

def make_graph(data):
    '''
      pt_BR: Retorna um grafico do documento
      en_US: Return a graph from document
    '''
    keys = data.keys()
    result = create_graph(data, keys)
    pos = networkx.spring_layout(result)
    networkx.draw(result, pos, node_color='#A0CBE2', edge_color='#BB0000', width=2, with_labels=True)
    plt.savefig("/tmp/simple_path.png") # save as png
    return result

def create_graph(data, key, parent = None):
    for k in key:
        value = data[k]
        arr = []
        if parent != None:
            if G.node.__contains__(str(k)) and G.node[str(k)]['data']['parent'] == parent:
                aux_node = G.node[str(k)]
                actual_value = aux_node['data']['value']
                actual_value.append(str(value))
                G.add_node(str(k), data={ "value":actual_value, "parent":str(parent) })
                G.add_edge(parent, str(k))
            else:
                arr.append(str(value))
                G.add_node(str(k), data={ "value":arr, "parent":str(parent) })
                G.add_edge(parent, str(k))
        else:
            if G.node.__contains__(str(k)):
                aux_node = G.node[str(k)]
                actual_value = aux_node['data']['value']
                actual_value.append(str(value))
                G.add_node(str(k), data={ "value":actual_value, "parent":str(parent) })
            else:
                arr.append(str(value))
                G.add_node(str(k), data={ "value":arr, "parent":str(parent) })

        #print 'nodes: ' + str(G.nodes(data=True))
        #print 'edges: ' + str(G.edges())

        if isinstance(value, dict):
            create_graph(value, value.keys(), k)
        elif isinstance(value, list):
            for l in value:
                if isinstance(l, dict):
                    create_graph(l, l.keys(), k)
    return G
