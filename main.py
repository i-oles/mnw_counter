import os
from string_operations import filter_first_files, split_duets, cut_char, display


DIRECTORY = 'R:\\p2-ogolna\\kolekcje_skonczone'
# DIRECTORY = 'C:\\Users\\ioles\\Pictures\\DO ZROBIENIA'
# DIRECTORY = 'R:\\p2-ogolna\\rozdzielnia'
COMPONENT = 'mnw'
F_EXT = 'tiff'
CHAR = '-'
SEARCH_01 = f'.*\(0?1\)\.{F_EXT}?$'
ones_all = []


for subdir, dirs, files in os.walk(DIRECTORY):
    ones_all = [filter_first_files(file, SEARCH_01) for file in files]

ones_splited = [split_duets(filename, COMPONENT) for filename in ones_all]
ones_without_mnw = [cut_char(obj, COMPONENT) for obj in ones_splited]
ones_unique = list(set(ones_without_mnw))
ones_short = [cut_char(obj, CHAR) for obj in ones_unique]
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


"""
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
