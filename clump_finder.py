__author__ = 'memery'

def find_clumps(genome, k, t, L):
    frequent_patterns = set()
    clumps = []
    for i in range(4**k -1):
        clumps.append(0)
    for i in range(len(genome) - L):
        text = genome[i:i+L]


def make_frequency_array(text, k):
    frequency_array = []
    for i in range(0, 4**k -1):
        frequency_array.append(i)
    for i in range(0, len(text) - k):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array