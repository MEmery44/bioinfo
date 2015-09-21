__author__ = 'memery'

import networkx as nx
from itertools import product
from random import choice


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


def add_random_eulerian_bridge(G):
    start_nodes = [x for x in G.in_degree() if G.in_degree(x) - G.out_degree(x) == 1]
    end_nodes = [x for x in G.in_degree() if G.in_degree(x) - G.out_degree(x) == -1]
    start_node, end_node = choice(start_nodes), choice(end_nodes)
    G.add_edge(start_node, end_node)
    answered = False
    while not answered:
        try:
            cycle = eulerian_cycle(G)
        except nx.exception.NetworkXError:
            pass
        else:
            answered = True
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


def make_de_bruijin_graph(*kmers):  # used to have a k. see if this matters
    graph = nx.DiGraph()
    for kmer in kmers:
        graph.add_edge(kmer[:-1], kmer[1:])
    return graph

def make_multi_de_bruijin_graph(*kmers):  # used to have a k. see if this matters
    graph = nx.MultiDiGraph()
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
    for i in cycle[:-k + 1]:
        reconstructed = '{}{}'.format(reconstructed, i[1][-1])
    return reconstructed


def make_double_string_graph(*double_kmers):
    graph = nx.DiGraph()
    for double_kmer in double_kmers:
        first, second = double_kmer.strip().split('|')
        graph.add_edge((first[:-1], second[:-1]), (first[1:], second[1:]))
    return graph


def reconstruct_double_string(graph, l, d):
    path = add_eulerian_bridge(graph)
    prefix_recon, suffix_recon = path[0][0][0], path[0][0][1]
    for i in path:
        prefix_recon = '{}{}'.format(prefix_recon, i[1][0][-1])
        suffix_recon = '{}{}'.format(suffix_recon, i[1][1][-1])
    reconstructed = '{}{}'.format(prefix_recon, suffix_recon[-d - l:])
    return reconstructed


def generate_binary_strings(size):
    return [''.join(x) for x in product('01', repeat=int(size))]


def max_non_contig(G):
    paths = []
    for v in G.nodes():
        if G.in_degree(v) != 1 or G.out_degree(v) != 1:
            if G.out_degree(v) > 0:
                for w in G.successors(v):
                    non_branching_path = [v, w]
                    while G.in_degree(w) == 1 and G.out_degree(w) == 1:
                        non_branching_path.extend(G.successors(w))
                        w = G.successors(w)
                    paths.append(non_branching_path)
        else:
            start_node = v
            if G.out_degree(v) == 1:
                for w in G.successors(v):
                    cycle = [v, w]
                    while G.in_degree(w) == 1 and G.out_degree(w) == 1:
                        cycle.extend(G.successors(w))
                        w = G.successors(w)
                        if w == start_node:
                            paths.append(cycle)
    return paths

def max_non_contig_w_edges(G):
    paths = []
    for v, w in G.edges():
        if v == 'AAAAGCGCCGCGAAACTTTAGCCAACCGTCGCTAGTGACTTAGGTTGGAGACTAACTAAGTAAAAAA':
            pass
        if G.in_degree(v) != 1 or G.out_degree(v) != 1:
            if G.out_degree(v) > 0:
                for w in G.successors(v):
                    non_branching_path = [v, w]
                    while G.in_degree(w) == 1 and G.out_degree(w) == 1:
                        non_branching_path.extend(G.successors(w))
                        [w] = G.successors(w)
                    paths.append(non_branching_path)
        else:
            start_node = v
            if G.out_degree(v) == 1:
                for w in G.successors(v):
                    cycle = [v, w]
                    while G.in_degree(w) == 1 and G.out_degree(w) == 1:
                        cycle.extend(G.successors(w))
                        w = G.successors(w)
                        if w == start_node:
                            paths.append(cycle)
    return paths

def printable_non_contigs(*contigs):
    paths = []
    for contig in sorted(contigs):
        path = contig[0]
        for suffix in contig[1:]:
            path = '{}{}'.format(path, suffix[-1])
        paths.append(path)
    return paths

if __name__ == '__main__':
    pass