__author__ = 'memery'

from collections import Counter

def frequent_words(text, length):
    patterns = Counter()
    for i in range(len(text) - length):
        patterns[text[i:i+length]] += 1
    return patterns.most_common()

def counter_ties(most_common):
    most_common_string, occurences = most_common[0]
    for candidate in most_common[1:]:
        if candidate[1] == occurences:
            most_common_string = '{} {}'.format(most_common_string, candidate[0])
        else:
            break
    return ' '.join(sorted(most_common_string.split(' ')))

def read_dataset(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        common = frequent_words(lines[0].strip(), int(lines[1].strip()))
        return counter_ties(common)


if __name__ == '__main__':
    print(frequent_words('TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT', 3))

