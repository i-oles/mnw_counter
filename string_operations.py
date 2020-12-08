import re


def filter_first_files(file, regex_query):
    first_file = re.findall(r'{0}'.format(regex_query), file)
    if first_file:
        return file


def split_duets(filename, component):
    filename = str(filename)
    counter = filename.count(component)
    if counter > 1:
        splited_file = filename.split(',')
        return [part for part in splited_file]
    else:
        return filename


def cut_char(obj, char):
    if char in obj:
        char_index = obj.find(char)
        part_before_char = obj[:char_index]
        return part_before_char
    else:
        return obj


def display(some_list):
    [print(x) for x in some_list]
