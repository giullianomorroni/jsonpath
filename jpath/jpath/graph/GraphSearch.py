'''
Created on 26/03/2013

@author: giulliano
'''

class graph_search(object):
    
    def search_node(self, key, graph):
        if not graph.node.__contains__(key):
            return None

        #Retorna o valor que existe em 'data'
        node = graph.node[key]
        return node

    def search_edge(self, key1, key2, graph):
        try:
            edge = graph.edge[key1][key2]
            return edge
        except KeyError:
            return None