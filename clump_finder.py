__author__ = 'memery'


def better_find_clumps(genome, k, t, L):
    frequent_patterns = set()
    clump = []
    for i in range(0, 4 ** k - 1):
        clump.append(0)
    text = genome[:L]
    frequency_array = make_frequency_array(text, k)
    for i in range(0, 4 ** k - 1):
        if frequency_array[i] >= t:
            clump[i] = 1
    for i in range(1, len(genome) - L):
        first_pattern = genome[i - 1:i - 1 + k]
        index = pattern_to_number(first_pattern)
        frequency_array[index] -= 1
        last_pattern = genome[i + L - k: i + L]
        index = pattern_to_number(last_pattern)
        frequency_array[index] += 1
        if frequency_array[index] >= t:
            clump[index] = 1
    for i in range(0, 4 ** k - 1):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    return frequent_patterns


def make_frequency_array(text, k):
    frequency_array = []
    for i in range(4 ** k):
        frequency_array.append(0)
    for i in range(len(text) - (k - 1)):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array


def pattern_to_number(pattern):
    if pattern == '':
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def symbol_to_number(symbol):
    symbol_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return symbol_dict[symbol]


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return '{}{}'.format(prefix_pattern, symbol)


def number_to_symbol(index):
    number_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return number_dict[index]


if __name__ == '__main__':
    with open('E-coli.txt') as data:
        genome = data.readlines()[0]
        clumps = better_find_clumps(genome, 9, 3, 500)
        answer = ' '.join(sorted(clumps))
        with open('output.txt', 'w+') as out:
            out.write(answer)
