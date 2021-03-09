

with open('3R_dgrp_frequencies.txt') as file:
    data = [line.rstrip('\n').split('\t') for line in file]

test = enumerate(data[0].split('\t'))

test1 = {'data1': 0, 'data2': 1, 'data3': 2}


for tup in test:
    if tup[0] == 554:
        print(tup[1])


for x in test1.values():
    print(x)


fake_dict = {s: idx for idx, s in enumerate(data[0].split('\t'))}

somelist = list()
for key in fake_dict.keys():
    if fake_dict[key] > 485:
        somelist.append(key)

