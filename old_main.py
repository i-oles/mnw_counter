import re
import os
from string_operations import display

# *********** KOLEKCJE SKONCZONE ************
directory = 'R:\\p2-ogolna\\kolekcje_skonczone'
directory = '/Volumes/MNW_OLES/jpg_mnw'
#^ to powinno isc jako zmienna z basha, bo chcemy uzyskac ogolny przypadek
# python read variable from bash

# *********** PLIKI PRZED POSTPRODUKCJA ************
# directory = 'C:\\Users\\ioles\\Pictures\\DO ZROBIENIA'
# directory = 'R:\\p2-ogolna\\rozdzielnia'

# filtering files with ordinal number (1) or (01) and else ordinal numbers.

# def find_files dir :

# file_list = os.walk(directory)

# 1. funkcyjki ktore operuja na liscie plikow w katalogu dajesz do nowego pliczku, potem mozna to ladnie otestowac (funkcja dostaje liste plikow i zwraca liste plikow)
# 2. main.py to w zasadzie:
    # walk(dir)

all_ones_list = []

for subdir, dirs, files in os.walk(directory):
    for file in files:
        first_file = re.findall(r'.*\(0?1\)\.jpg?$', file)
        if first_file:
            all_ones_list.append(file)

# spliting filenames which include two object names

splited_duet_files = []
rest_ones = []
for filename in all_ones_list:
    count_mnw = filename.count('mnw')
    if count_mnw > 1:
        splited_file = filename.split(',')
        for part in splited_file:
            splited_duet_files.append(part)
    else:
        rest_ones.append(filename)

# adding splited filenames to the rest
[rest_ones.append(part) for part in splited_duet_files]

# slicing files to receive only prefix and digit (with possibly letters and _ after digit)
ones_without_mnw = []
for filename in rest_ones:
    i_after_digit = filename.find('mnw')
    before_mnw = filename[:i_after_digit]
    ones_without_mnw.append(before_mnw)

# removing all duplicates
unique_ones = list(set(ones_without_mnw))

# removing objects sets - leave only single objects

only_singles = []

for single_obj in unique_ones:
    if '-' in single_obj:
        hyphen_index = single_obj.find('-')
        part_before_hyphen = single_obj[:hyphen_index]
        only_singles.append(part_before_hyphen)
    else:
        only_singles.append(single_obj)

# making dict from only_singles and unique_ones
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


display(all_ones_list)
display(splited_duet_files)
display(ones_without_mnw)
display(unique_ones)
display(only_singles)
display(singles)
display(obj_sets)



"""counter_singles = len(singles)
[print(o) for o in singles]
print(f'photographed objects: {counter_singles}')
print('*****************************')
counter_sets = len(obj_sets)
[print(s) for s in obj_sets]
print(f'photographed sets: {counter_sets}')"""




if __name__ == '__main__':
    pass
