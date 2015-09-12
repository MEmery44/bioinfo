__author__ = 'memery'

import sys

def get_composition(k, text):
    composition_list = []
    for i in range(0, len(text)-k):
        composition_list.append(text[i:i+k])
    return composition_list


if __name__ == '__main__':
    with open('dataset_197_3.txt') as data:
        k = int(data.readline())
        text = data.readline().strip('')
        results = sorted(get_composition(k, text))
        with open('output.txt','w+') as out:
            for result in results:
                out.write(result + '\n')
