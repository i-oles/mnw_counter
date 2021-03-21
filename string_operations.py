from itertools import chain

class StringOperations:
    @staticmethod
    def split_two_items(filename_list, delimiter, tag):
        result_list1 = []
        result_list2 = []
        for filename in filename_list:
            counter = filename.count(tag)
            if counter > 1:
                two_items_splited = filename.split(delimiter)
                for item in two_items_splited:
                    result_list1.append(item)
            elif counter == 0:
                pass
            else:
                result_list2.append(filename)
        return chain(result_list1, result_list2)

    @staticmethod
    def cut_in_char(item, char):
        item = str(item)
        if char in item:
            char_index = item.find(char)
            part_before_char = item[:char_index]
            return part_before_char
        else:
            return item

    @staticmethod
    def add_ones_to_multi_keys_dict(zipped_list, default_dict):
        [default_dict[i[0]].append(i[1]) for i in zipped_list]

