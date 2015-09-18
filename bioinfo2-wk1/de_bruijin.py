__author__ = 'memery'

from collections import defaultdict

def make_bruijin(k, text):
    graph = defaultdict(list)
    for i in range(len(text) -k+1):
        graph[text[i:i+k-1]].append(text[i+1:i+k])
    return graph

def make_debruijin_from_kmer(kmer_list):
    graph = defaultdict(list)
    for kmer in kmer_list:
        graph[kmer[:-1]].append(kmer[1:])
    return graph

def print_overlap_graph(graph):
    for i, j in sorted(graph.items()):
        print('{} -> {}'.format(i, ','.join(sorted(j))))

def write_overlap_graph(graph):
    with open('output.txt', 'w+') as out:
        for i, j in sorted(graph.items()):
            out.writelines('{} -> {}\n'.format(i, ','.join(sorted(j))))

if __name__ == '__main__':
    with open('dataset_200_7.txt') as data:
        kmers = [x.strip() for x in data.readlines()]
    graph = make_debruijin_from_kmer(kmers)
    write_overlap_graph(graph)