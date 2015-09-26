__author__ = 'memery'


def translate_protein(rna_string):
    rna_dict = TRANSLATE_DICT
    translated_string = ''
    for i in range(len(rna_string) // 3):
        translated_string = '{}{}'.format(translated_string, rna_dict[rna_string[3 * i:3 * i + 3]])
        if rna_dict[rna_string[3 * i:3 * i + 3]] == '':
            break
    return translated_string


def make_translate_dict(rna_txt):
    rna_dict = {}
    with open(rna_txt) as data:
        for line in data.readlines():
            rna_dict[line.split(' ')[0]] = line.split(' ')[1].strip()
    return rna_dict


TRANSLATE_DICT = make_translate_dict('RNA_codon_table_1.txt')


def reverse_dna(dna):
    dna_dict = {'A': 'T',
                'C': 'G',
                'G': 'C',
                'T': 'A'}
    new_dna = []
    for i in range(len(dna)):
        new_dna.append(dna_dict[dna[i]])
    return ''.join(reversed(new_dna))


def transcribe_dna(dna):
    return dna.translate({ord(x): y for (x, y) in zip('T', 'U')})


def encode_peptide(dna, peptide):
    encoding_dna = []
    for i in range(len(dna) - len(peptide) * 3):
        if translate_protein(transcribe_dna(dna)[i:i + 3 * len(peptide)]) == peptide:
            encoding_dna.append(dna[i:i + 3 * len(peptide)])
        if translate_protein(transcribe_dna(reverse_dna(dna[i:i + 3 * len(peptide)]))) == peptide:
            encoding_dna.append(dna[i:i + 3 * len(peptide)])
    return encoding_dna

def number_of_cyclopeptides(n):
    return n * (n-1)



if __name__ == '__main__':
    print(number_of_cyclopeptides(23856))
