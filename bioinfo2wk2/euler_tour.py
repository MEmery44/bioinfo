__author__ = 'memery'

from collections import defaultdict
import networkx as nx
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


def make_graph_default(*edges):
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge.split(' -> ')
        if ',' in end:
            for node in end.split(','):
                graph[start].append((node.strip(), False))
        else:
            graph[start].append((end.strip(), False))
    return graph


def default_eulerian_cycle(graph):
    """

    :param graph:
    :type graph: defaultdict
    """
    to_be_traveled = graph.copy()
    path = []
    new_node = choice(list(graph.keys()))
    path.append(new_node[0])
    while len(to_be_traveled) != 0:
        node = to_be_traveled[new_node[0]]
        if
        if type(node) == list:
            new_node = choice(node)
            new_node = new_node[0], True
        else:
            if new
            new_node = node
            new_node = new_node[0], True
        path.append(new_node[0])
    return path


def print_eulerian(*euler):
    path = euler[0][0]
    for i in range(len(euler)):
        path = '{}->{}'.format(path, euler[i][1])
    return path


if __name__ == '__main__':
    graph = make_graph_default(
        *('0 -> 3', '1 -> 0', '2 -> 1,6', '3 -> 2', '4 -> 2', '5 -> 4', '6 -> 5,8', '7 -> 9', '8 -> 7', '9 -> 6'))
    print(default_eulerian_cycle(graph))
