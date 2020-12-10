import os
import re
from string_operations import split_duets, cut_char, display
from itertools import chain

#DIRECTORY = 'R:\\p2-ogolna\\kolekcje_skonczone'
DIRECTORY = '/Volumes/MNW_OLES/jpg_mnw'

COMPONENT = 'mnw'
F_EXT = 'jpg'
CHAR_H = '-'
CHAR_C = ','
SEARCH_01 = f'.*\(0?1\)\.{F_EXT}?$'


ones_all = []
for subdir, dirs, files in os.walk(DIRECTORY):
    for file in files:
        first_file = re.findall(r'{}'.format(SEARCH_01), file)
        if first_file:
            ones_all.append(file)

ones_splited = list(split_duets(ones_all, CHAR_C))
ones_without_mnw = [cut_char(obj, COMPONENT) for obj in ones_splited]
ones_unique = list(set(ones_without_mnw))
ones_short = [cut_char(obj, CHAR_H) for obj in ones_unique]
ones_zipped = zip(ones_short, ones_unique)
ones_dict = dict(ones_zipped)
singles_short = list(set(ones_short))
ones_dict_keys = ones_dict.keys()

singles_long = []
sets_long = ones_unique

for obj in ones_short:
    if obj in ones_dict_keys:
        singles_long.append(ones_dict[obj])
        sets_long.remove(ones_dict[obj])


display(ones_all)
display(ones_splited)
display(ones_without_mnw)
display(ones_unique)
display(ones_short)
display(ones_dict)
display(singles_long)
display(sets_long)



counter_singles = len(singles_long)
[print(o) for o in singles_long]
print(f'photographed objects: {counter_singles}')
print('*****************************')
counter_sets = len(sets_long)
[print(s) for s in sets_long]
print(f'photographed sets: {counter_sets}')
"""

if __name__ == '__main__':
    pass
