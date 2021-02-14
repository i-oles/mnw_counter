from itertools import chain


class ReportFile:
    one_empty_line = '\n'
    two_empty_lines = '\n\n'

    @staticmethod
    def create_new_file(path, dir_name, date):
        result_file = open(f'{path}/{dir_name}/{date}.txt', 'w')
        return result_file

    @staticmethod
    def add_date_line(date, space):
        date_line = f'Date: {date}{space}'
        return date_line

    @staticmethod
    def add_counting_result_line(num, space):
        counting_result_line = f'You had taken pictures of {num} objects.{space}'
        return counting_result_line

    @staticmethod
    def add_label_line(label):
        label_singles = f'{label.text()}'
        return label_singles

    @staticmethod
    def write_lines(file, func, line):
        file.writelines(func(line))

    """
        result_file.writelines(self.__list_format(self.singles_long))
        result_file.write(two_empty_lines)
        if self.listWidgetSets.count() != 0:
            label_sets = f'{self.labelListSets.text()} {one_empty_line}'
            result_file.write(label_sets)
            result_file.writelines(self.__list_format(self.sets_long))
        result_file.close()
    """
    @staticmethod
    def create_new_result_file(path, result_dir_name, current_date):
        result_file = open(r'{}/{}/{}.txt'.format(path, result_dir_name, current_date), 'w')
        return result_file


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
