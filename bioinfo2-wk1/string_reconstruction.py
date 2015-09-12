__author__ = 'memery'

def make_genome_string(list_of_strings):
    genome_string = list_of_strings[0]
    for additional_string in list_of_strings[1:]:
        genome_string = '{}{}'.format(genome_string, additional_string[-1])
    return genome_string

if __name__ == '__main__':
    with open('dataset_198_3.txt') as data:
        reads = []
        lines = data.readlines()
        for line in lines[:]:
            reads.append(line.strip())
        result = make_genome_string(reads)
        with open('output.txt', 'w+') as out:
            out.write(result)