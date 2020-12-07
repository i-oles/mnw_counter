import re
import os
from string_operations import *



DIRECTORY = ''
FILE_EXTENTION = 'jpg'
COMPONENT = 'mnw'
CHAR = '-'
all_first_files = []

for subdir, dirs, files in os.walk(directory):
    all_first_files = [filter_first_files(file) for file in files]

# spliting filenames which include two object names
splited_files = [split_duet(filename, COMPONENT) for filename in all_first_files]

# slicing files to receive only prefix and digit (with possibly letters and _ after digit)
ones_without_mnw = list(cut_char(obj, COMPONENT) for obj in splited_files)

# removing all duplicates
unique_ones = list(set(ones_without_mnw))

# removing objects sets - leave only single objects
only_singles = list(cut_char(obj, CHAR) for obj in unique_ones)

objects_zipped = zip(only_singles, unique_ones)
objects_dict = dict(objects_zipped)

only_singles = list(set(only_singles))

singles = []
obj_sets = unique_ones

objects_dict_keys = objects_dict.keys()
for obj in only_singles:
    if obj in objects_dict_keys:
        singles.append(objects_dict[obj])
        obj_sets.remove(objects_dict[obj])

singles = filter()


counter_singles = len(singles)
[print(o) for o in singles]
print(f'photographed objects: {counter_singles}')
print('*****************************')
counter_sets = len(obj_sets)
[print(s) for s in obj_sets]
print(f'photographed sets: {counter_sets}')




if __name__ == '__main__':
    pass
