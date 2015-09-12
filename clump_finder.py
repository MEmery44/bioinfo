__author__ = 'memery'


def find_clumps(genome, k, t, L):
    frequent_patterns = set()
    clumps = []
    for i in range(4 ** k - 1):
        clumps.append(0)
    for i in range(len(genome) - L):
        text = genome[i:i + L]


def make_frequency_array(text, k):
    frequency_array = []
    for i in range(0, 4 ** k - 1):
        frequency_array.append(i)
    for i in range(0, len(text) - k):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        pass


def pattern_to_number(pattern):
    if pattern == '':
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def symbol_to_number(symbol):
    symbol_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return symbol_dict[symbol]

if __name__ == '__main__':
    print(pattern_to_number('TCTCAACTGAGGAGTT'))
