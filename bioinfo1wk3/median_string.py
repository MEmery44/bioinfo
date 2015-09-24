__author__ = 'memery'

from itertools import product


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
        if get_profile_score(text[i:i + k], matrix) > profile_score:
            profile_score = get_profile_score(text[i:i + k], matrix)
            profile_text = text[i:i + k]
    return profile_text


def get_profile_score(text, matrix):
    dna_map = {'A': 0,
               'C': 1,
               'G': 2,
               'T': 3}
    total = 1
    for i in range(len(text)):
        total *= matrix[dna_map[text[i]]][i]
    return total


def make_matrix(*strings):
    matrix = []
    for line in strings:
        matrix.append([float(x) for x in line.split(' ')])
    return matrix


if __name__ == '__main__':
    with open('dataset_159_3.txt') as data:
        lines = [x.strip() for x in data.readlines()]
        matrix = make_matrix(*(lines[2:]))
        print(profile_most_probable_kmer(lines[0], int(lines[1]), matrix))
