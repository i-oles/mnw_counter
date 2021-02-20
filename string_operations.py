from itertools import chain


class FileContent:
    @staticmethod
    def add_date(file, date, space):
        return file.write(f'Date: {date}{space}')

    @staticmethod
    def add_count_result(file, num, space):
        return file.write(f'You had taken pictures of {num} objects.{space}')

    @staticmethod
    def add_label(file, label, space):
        return file.write(f'{label.text()}{space}')

    @staticmethod
    def add_list_view(file, func, space):
        lines = file.writelines(func)
        file.write(f'{space}')
        return lines

    @staticmethod
    def close_file(file):
        return file.close()


class StringOperations:
    @staticmethod
    def split_two_items(start_list, char, component):
        result_list1 = []
        result_list2 = []
        for filename in start_list:
            counter = filename.count(component)
            if counter > 1:
                two_items_splited = filename.split(char)
                for item in two_items_splited:
                    result_list1.append(item)
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
