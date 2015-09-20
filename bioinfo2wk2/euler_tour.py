__author__ = 'memery'

import networkx as nx
from itertools import product


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
            prefix, suffix = cycle[:i], cycle[i + 1:]
            del cycle[i]
            cycle = suffix + prefix
            break
    return cycle


def print_eulerian(*euler):
    path = euler[0][0]
    for i in range(len(euler)):
        path = '{}->{}'.format(path, euler[i][1])
    return path


def make_de_bruijin_graph(*kmers): #used to have a k. see if this matters
    graph = nx.DiGraph()
    for kmer in kmers:
        graph.add_edge(kmer[:-1], kmer[1:])
    return graph

def reconstruct_string(graph):
    path = add_eulerian_bridge(graph)
    reconstructed = path[0][0]
    for i in path:
        reconstructed = '{}{}'.format(reconstructed, i[1][-1])
    return reconstructed

def reconstruct_uni_string(k, graph):
    cycle = eulerian_cycle(graph)
    reconstructed = cycle[0][0]
    for i in cycle[:-k+1]:
        reconstructed = '{}{}'.format(reconstructed, i[1][-1])
    return reconstructed


def generate_binary_strings(size):
    return [''.join(x) for x in product('01', repeat=int(size))]

if __name__ == '__main__':
    graph = make_de_bruijin_graph(*generate_binary_strings(8))
    with open('output.txt', 'w+') as out:
        out.write(reconstruct_uni_string(8, graph))
    # print(reconstruct_uni_string(4, graph))
