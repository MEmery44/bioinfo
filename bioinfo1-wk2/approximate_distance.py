__author__ = 'memery'


def get_approximate_match(pattern, text, d):
    approx_matches = []
    for i in range(len(text) - len(pattern) + 1):
        hamming = get_hamming_distance(pattern, text[i:i + len(pattern)])
        if hamming <= d:
            approx_matches.append(i)
    return ' '.join(str(x) for x in approx_matches)


def get_approximate_pattern_count(pattern, text, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        test_pattern = text[i:i + len(pattern)]
        if get_hamming_distance(test_pattern, pattern) <= d:
            count += 1
    return count


def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance


if __name__ == '__main__':
    with open('dataset_9_6.txt') as data:
        line1, line2, line3 = data.readlines()
    count = get_approximate_pattern_count(line1.strip(), line2.strip(), int(line3))
    print(count)
    # with open('output.txt', 'w+') as out:
    #     out.write(match)
