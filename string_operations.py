import re
from main import FILE_EXTENTION
from configurations import *


def filter_first_files(file):
    first_file = re.findall(r'.*\(0?1\)\.{}?$'.format(FILE_EXTENTION), file)
    if first_file:
        return file


def split_duets(filename, component):
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
        yield part_before_char
    else:
        yield obj


def

