from itertools import chain


class StringOperations:
    @staticmethod
    def split_duets(start_list, char, component):
        result_list1 = []
        result_list2 = []
        for filename in start_list:
            counter = filename.count(component)
            if counter > 1:
                split_duet = filename.split(char)
                for one in split_duet:
                    result_list1.append(one)
            else:
                result_list2.append(filename)
        return chain(result_list1, result_list2)

    @staticmethod
    def cut_char(item, char):
        item = str(item)
        if char in item:
            char_index = item.find(char)
            part_before_char = item[:char_index]
            return part_before_char
        else:
            return item
