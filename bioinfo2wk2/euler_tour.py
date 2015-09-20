__author__ = 'memery'

import networkx as nx



def eulerian_cycle(graph):
    return [i for i in nx.eulerian_circuit(graph)]


def make_graph(*edges):
    graph = nx.DiGraph()
    for edge in edges:
        start, end = edge.split(' -> ')
        if ',' in end:
            for node in end.split(','):
                graph.add_edge(start, node.strip())
        else:
            graph.add_edge(start, end.strip())
    return graph



def add_eulerian_bridge(G):
    [start_node] = [x for x in G.in_degree() if G.in_degree(x) - G.out_degree(x) == 1]
    [end_node] = [x for x in G.in_degree() if G.in_degree(x) - G.out_degree(x) == -1]
    G.add_edge(start_node, end_node)
    cycle = eulerian_cycle(G)
    for i in range(len(cycle)):
        if cycle[i] == (start_node, end_node):
            prefix, suffix = cycle[:i], cycle[i+1:]
            del cycle[i]
            cycle = suffix + prefix
            break
    return cycle


def print_eulerian(*euler):
    path = euler[0][0]
    for i in range(len(euler)):
        path = '{}->{}'.format(path, euler[i][1])
    return path

def make_de_bruijin_graph(k, *kmwers):
    grsph = nx.



if __name__ == '__main__':
    with open('dataset_203_5.txt') as data:
        graph = make_graph(*(x.strip() for x in data.readlines()))
    cycle = add_eulerian_bridge(graph)
    with open('output.txt', 'w+') as out:
        out.write(print_eulerian(*cycle))
