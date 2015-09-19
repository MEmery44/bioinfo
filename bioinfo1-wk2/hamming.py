__author__ = 'memery'

def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance

if __name__ == '__main__':
    print(get_hamming_distance('CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG', 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'))