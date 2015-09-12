__author__ = 'memery'

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count

def read_dataset(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return pattern_count(lines[0].strip(), lines[1].strip())

if __name__ == '__main__':
    print(read_dataset('dataset_2_6.txt'))