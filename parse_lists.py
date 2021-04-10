class FilterFilenames:
    def __init__(self, filenames):
        self.filenames = filenames

    tag = 'mnw'
    delimiter = ','

    def split_filename():
        result_list1 = []
        result_list2 = []
        for filename in filenames:
            counter = filename.count(tag)
            if counter > 1:
                two_items_splited = filename.split(delimiter)
                for item in two_items_splited:
                    result_list1.append(item)
            elif counter == 0:
                pass
            else:
                result_list2.append(filename)
        return result_list1 + result_list2


def make_singles_and_set_list(self):
    ones_separated = list(StringOperations.split_two_items(self.ones_all, self.coma_char, self.component))
    ones_without_mnw = [StringOperations.cut_in_char(item, self.component) for item in ones_separated]
    ones_unique = sorted(list(set(ones_without_mnw)))
    ones_short = [StringOperations.cut_in_char(item, self.hyphen_char) for item in ones_unique]
    ones_zipped = list(zip(ones_short, ones_unique))
    ones_in_multi_keys_dict = defaultdict(list)
    StringOperations.add_ones_to_multi_keys_dict(ones_zipped, ones_in_multi_keys_dict)
    singles_short = list(set(ones_short))
    ones_dict_keys = ones_in_multi_keys_dict.keys()

    self.singles_long = []
    self.sets_long = ones_unique.copy()
    for item in singles_short:
        if item in ones_dict_keys:
            self.singles_long.append(ones_in_multi_keys_dict[item][0])
            self.sets_long.remove(ones_in_multi_keys_dict[item][0])
    self.singles_long = sorted(self.singles_long)
    self.sets_long = sorted(self.sets_long)
    return self.singles_long, self.sets_long



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