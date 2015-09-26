__author__ = 'memery'

from itertools import product
import numpy as np
from collections import Counter


def distance_between_pattern_and_string(pattern, dna):
    distance = 0
    for text in dna:
        hamming_distance = float('infinity')
        for i in range(len(text) - len(pattern)):
            if hamming_distance > get_hamming_distance(pattern, text[i:i + len(pattern)]):
                hamming_distance = get_hamming_distance(pattern, text[i:i + len(pattern)])
        distance += hamming_distance
    return distance


def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance


def median_string(dna, k):
    distance = float('infinity')
    for pattern in generate_dna_strings(k):
        if distance > distance_between_pattern_and_string(pattern, dna):
            distance = distance_between_pattern_and_string(pattern, dna)
            median = pattern
    return median


def generate_dna_strings(size):
    return [''.join(x) for x in product('ACGT', repeat=int(size))]


def profile_most_probable_kmer(text, k, matrix):
    profile_score = 0
    profile_text = ''
    for i in range(len(text) - k):
        if get_profile_score(text[i:i + k], matrix) >= profile_score:
            profile_score = get_profile_score(text[i:i + k], matrix)
            profile_text = text[i:i + k]
    return profile_text


def get_profile_score(text, matrix):
    dna_map = {'A': 0,
               'C': 1,
               'G': 2,
               'T': 3}
    total = 0
    for i in range(len(text)):
        total += matrix[dna_map[text[i]]][i]
    return total


def make_matrix(*strings):
    matrix = []
    for line in strings:
        matrix.append([float(x) for x in line.split(' ')])
    return matrix


def build_profile_from_strings(strings):
    matrix = np.ones(shape=(4, len(strings[0])), dtype=np.float)
    dna_map = {'A': 0,
               'C': 1,
               'G': 2,
               'T': 3}
    for text in strings:
        for i in range(len(text)):
            matrix[dna_map[text[i]], i] += 1
    matrix /= len(strings)
    return matrix.tolist()


def get_score(strings):
    total_count = 0
    matrix = np.array([list(string) for string in strings])
    for i in range(len(strings[0])):
        count = Counter(matrix[:, i])
        total_count += len(strings) - count.most_common(1)[0][1]
    return total_count


def greedy_motif_search(dna, k, t):
    best_motifs = [text[0:k] for text in dna]
    for i in range(len(dna[0]) - k):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            matrix = build_profile_from_strings(motifs)
            new_motif = profile_most_probable_kmer(dna[j], k, matrix)
            motifs.append(new_motif)
        if get_score(motifs) <= get_score(best_motifs):
            best_motifs = motifs
    return best_motifs

if __name__ == '__main__':
    with open('greedy_pseudo.txt') as data:
        k, t = data.readline().split(' ')
        lines = [x.strip() for x in data.readlines()]
    print('\n'.join(greedy_motif_search(lines, int(k), int(t))))
    # print('\n'.join(['GTACATCTCTCT', 'GTCGATATCTCG', 'GTTGATATCTCG', 'GTAGGTATCTCT', 'GTGGATATCGCT', 'GTCGTTATCCCA', 'GTAGATATCCCT', 'GTGGTTATCACG', 'GTGGTTATCCCA', 'GTGGCTATCGCC', 'GTGGATATCCCT', 'GTCGTTATCACA', 'GTTGGTATCACT', 'GTTGATATCTCT', 'GTAGGTATCACC', 'GTGGCTATCGCT', 'GTGGGTATCTCA', 'GTCGATATCGCT', 'GTTGATATCTCC', 'GTTGGTATCACC', 'GTAGGTATCACT', 'GTCGTTATCCCG', 'GTAGGTACATCA', 'GTGGTTATCACC', 'GTTGTTATCGCA']))
    # with open('greedy_out.txt') as out:
    #     print(get_score([x.strip() for x in out.readlines()]))