__author__ = 'memery'


def motif_enumeration(dna, k, d):
    patterns = set()
    for i in range(0, len(dna[0]) - k + 1):
        pattern = dna[0][i:i + k]
        for new_pattern in neighbours(pattern, d):
            string_match = True
            for dna_string in dna:
                curr_string_match = False
                for j in range(0, len(dna_string) - k + 1):
                    if get_hamming_distance(new_pattern, dna_string[j:j + k]) <= d:
                        curr_string_match = True
                        break
                if not curr_string_match:
                    string_match = False
                    break
            if string_match:
                patterns.add(new_pattern)
    return patterns


def pretty_output(*patterns):
    return ' '.join(sorted(list(patterns)))


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


def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance

def distance_between_patterns_and_strings(pattern, dna):
    pass

if __name__ == '__main__':
    with open('dataset_156_7.txt') as data:
        k, d = data.readline().split()
        dna = [line.strip() for line in data.readlines()]
        patterns = motif_enumeration(dna, int(k), int(d))
        print(pretty_output(*patterns))
