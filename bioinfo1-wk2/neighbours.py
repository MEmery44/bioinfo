from hamming import get_hamming_distance
from clump_finder import pattern_to_number, number_to_pattern
from approximate_distance import get_approximate_pattern_count

__author__ = 'memery'


def immediate_neighbours(pattern):
    neighbourhood = {pattern}
    for i in range(len(pattern)):
        nucleotides = {'A', 'C', 'G', 'T'}
        symbol = pattern[i]
        nucleotides.remove(symbol)
        for nucleotide in nucleotides:
            neighbour = list(pattern)
            neighbour[i] = nucleotide
            neighbourhood.add(''.join(neighbour))
    return neighbourhood


def neighbours(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighbourhood = set()
    suffix_neighbours = neighbours(pattern[1:], d)
    for suffix_string in suffix_neighbours:
        if get_hamming_distance(pattern[1:], suffix_string) < d:
            for i in {'A', 'C', 'G', 'T'}:
                neighbourhood.add('{}{}'.format(i, suffix_string))
        else:
            neighbourhood.add('{}{}'.format(pattern[0], suffix_string))
    return neighbourhood


def return_spaced(*sequence):
    return ' '.join(sorted(sequence))


def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = set()
    close, frequency_array = [], []
    print('Step 1')
    for i in range(0, 4 ** k):
        close.append(0)
        frequency_array.append(0)
    print('Step 2')
    for i in range(0, len(text) - k + 1):
        neighbourhood = neighbours(text[i:i + k], d)
        for pattern in neighbourhood:
            index = pattern_to_number(pattern)
            close[index] = 1
    print('Step 3')
    for i in range(0, 4 ** k):
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            frequency_array[i] = get_approximate_pattern_count(pattern, text, d)
    max_count = max(frequency_array)
    print('Step 4')
    for i in range(0, 4 ** k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    return frequent_patterns


def frequent_words_with_mismatches_w_complement(text, k, d):
    frequent_patterns = set()
    close, frequency_array = [], []
    print('Step 1')
    for i in range(0, 4 ** k):
        close.append(0)
        frequency_array.append(0)
    print('Step 2')
    for i in range(0, len(text) - k + 1):
        neighbourhood = neighbours(text[i:i + k], d)
        for pattern in neighbourhood:
            index = pattern_to_number(pattern)
            close[index] = 1
    print('Step 3')
    for i in range(0, 4 ** k):
        if i % 1000 == 0:
            print(1)
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            frequency_array[i] = get_approximate_pattern_count(pattern, text, d) + \
                                 get_approximate_pattern_count(reverse_dna(pattern), text, d)
    max_count = max(frequency_array)
    print('Step 4')
    for i in range(0, 4 ** k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    return frequent_patterns


def reverse_dna(dna):
    dna_dict = {'A': 'T',
                'C': 'G',
                'G': 'C',
                'T': 'A'}
    new_dna = []
    for i in range(len(dna)):
        new_dna.append(dna_dict[dna[i]])
    return ''.join(reversed(new_dna))


if __name__ == '__main__':
    neighbourhood = neighbours('TGCAT', 2)
    print(len(neighbourhood))
