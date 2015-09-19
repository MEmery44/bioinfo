import hamming

__author__ = 'memery'



print(hamming.get_hamming_distance('ABC', 'ABD'))

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


def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance


if __name__ == '__main__':
    print(immediate_neighbours('AAA'))
