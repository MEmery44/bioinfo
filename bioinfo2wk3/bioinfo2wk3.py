__author__ = 'memery'

import difflib
from itertools import chain, combinations


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
    return n * (n - 1)


MASS_DICT = {'G': 57,
             'A': 71,
             'S': 87,
             'P': 97,
             'V': 99,
             'T': 101,
             'C': 103,
             'I': 113,
             'L': 113,
             'N': 114,
             'D': 115,
             'K': 128,
             'Q': 128,
             'E': 129,
             'M': 131,
             'H': 137,
             'F': 147,
             'R': 156,
             'Y': 163,
             'W': 186}


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def get_powerset_spectrum(power_set):
    return sorted((sum(MASS_DICT[i] for i in chopped)) for chopped in power_set)

def get_linear_spectrum(peptide):
    prefix_mass = [0]
    for i in range(1, len(peptide) + 1):
        prefix_mass.append(prefix_mass[i - 1] + MASS_DICT[peptide[i - 1]])
    linear_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) +1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(linear_spectrum)

def get_cyclic_spectrum(peptide):
        prefix_mass = [0]
        for i in range(1, len(peptide) + 1):
            prefix_mass.append(prefix_mass[i - 1] + MASS_DICT[peptide[i - 1]])
        peptide_mass = sum(MASS_DICT[peptide[x]] for x in range(len(peptide)))
        cyclical_spectrum = [0]
        for i in range(len(peptide)):
            for j in range(i + 1, len(peptide) +1):
                cyclical_spectrum.append(prefix_mass[j] - prefix_mass[i])
                if i > 0 and j < len(peptide):
                    cyclical_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
        return sorted(cyclical_spectrum)

if __name__ == '__main__':
    print(' '.join(str(x) for x in get_cyclic_spectrum(('KIHPNQMTFTVI'))))
