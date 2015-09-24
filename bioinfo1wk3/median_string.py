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

if __name__ == '__main__':
    with open('dataset_158_9.txt') as data:
        lines = [x.strip() for x in data.readlines()]
        print(median_string(lines[1:], int(lines[0])))
