__author__ = 'memery'

def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    distance = 0
    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance

if __name__ == '__main__':
    with open('dataset_9_3.txt') as data:
        line1, line2 = data.readlines()
    hamming = get_hamming_distance(line1.strip(), line2.strip())
    print(hamming)