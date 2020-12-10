from itertools import chain


def split_duets(start_list, char):
    result_list1 = []
    result_list2 = []
    for filename in start_list:
        counter = filename.count('mnw')
        if counter > 1:
            split_duet = filename.split(char)
            for one in split_duet:
                result_list1.append(one)
        else:
            result_list2.append(filename)
    return chain(result_list1, result_list2)


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
    #print(some_list)
    #[print(i) for i in some_list]
    #print(type(some_list))
    print(f"some list: {counter} objects.")
