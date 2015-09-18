__author__ = 'memery'
import sys
from collections import defaultdict

def make_overlap_graph(nodes):
    overlap_graph = defaultdict(set)
    for node in nodes:
        for other in nodes:
            if node != other and node[1:] == other[:-1]:
                overlap_graph[node] = other
    return overlap_graph

def print_overlap_graph(graph):
    for i, j in graph.items():
        print('{} -> {}'.format(i, j))

def write_overlap_graph(graph):
    with open('output.txt', 'w+') as out:
        for i, j in sorted(graph.items()):
            out.writelines('{} -> {}\n'.format(i, j))

if __name__ == '__main__':
    with open('dataset_198_9.txt') as data:
        nodes = [x.strip() for x in data.readlines()]
    graph = make_overlap_graph(nodes)
    print_overlap_graph(graph)