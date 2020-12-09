import re


def split_duets(filename):
    counter = filename.count('mnw')
    if counter > 1:
        splited_file = filename.split(',')
        for part in splited_file:
            return part


def cut_char(obj, char):
    obj = str(obj)
    if char in obj:
        char_index = obj.find(char)
        part_before_char = obj[:char_index]
        return part_before_char
    else:
        return obj



def display(some_list):
    counter = len(some_list)
    #[print(i) for i in some_list]
    print(f"some list: {counter} objects.")
