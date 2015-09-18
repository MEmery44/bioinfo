__author__ = 'memery'

def make_skew(skew_string):
    skew = 0
    skew_list = [0]
    for i in range(0, len(skew_string)):
        if skew_string[i] == 'C':
            skew -=1
        elif skew_string[i] == 'G':
            skew += 1
        skew_list.append(skew)
    return skew_list

def min_skew(*skew_list):
    current_min = float('inf')
    min_list = []
    for position, skew in enumerate(skew_list):
        if skew < current_min:
            min_list = [position]
            current_min = skew
        elif skew == current_min:
            min_list.append(position)
    return ' '.join(str(x) for x in min_list)

if __name__ == '__main__':
    with open('dataset_7_6.txt') as data:
        line1 = data.read()
    skew_list = make_skew(line1)
    skew = min_skew(*skew_list)
    print(skew)
