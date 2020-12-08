import re


def filter_first_files(file, regex_formula):
    file = str(file)
    first_file = re.findall(r'.*\(0?1\)\.jpg?$', file)
    if first_file:
        return file


def split_duets(filename, component):
    filename = str(filename)
    counter = filename.count(component)
    if counter > 1:
        splited_file = filename.split(',')
        for part in splited_file:
            return part
    else:
        return filename


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
    print(f"some list: {counter} objects.")
