from datetime import date
import os


class ExportToFile:
    report_dir_name = 'Daily_Reports'

    current_date = date.today()
    current_date.strftime("%d-%m-%Y")

    one_empty_line = '\n'
    two_empty_lines = '\n\n'

    def __init__(self, dir_path, count_result, singles_list, sets_list, widget):
        self.dir_path = dir_path
        self.count_result = count_result
        self.singles_long = singles_list
        self.sets_long = sets_list
        self.widget = widget

        self.report_dir_path = f'{self.dir_path}/{self.report_dir_name}'

        self.preparations_before_write()
        self.write_content()
        self.report_file.close()

    def preparations_before_write(self):
        self.make_dir_if_not_exist(self.report_dir_path)
        self.make_empty_report_file(self.report_dir_path, self.current_date)

    def make_dir_if_not_exist(self, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    def make_empty_report_file(self, dir_path, date):
        write_mode = 'w'
        self.report_file = open(f'{dir_path}/{date}.txt', write_mode)

    def write_content(self):
        self.report_file.write(f'Date: {self.current_date}{self.two_empty_lines}')
        self.report_file.write(f'You had taken pictures of {self.count_result} objects.{self.two_empty_lines}')
        self.report_file.write(f'Photographed:{self.one_empty_line}')
        self.write_objects_list(self.report_file, self.list_view(self.singles_long))
        if self.widget.count() > 0:
            self.report_file.write(f'Additional images contain objects in sets:{self.one_empty_line}')
            self.write_objects_list(self.report_file, self.list_view(self.sets_long))

    def write_objects_list(self, file, func):
        lines = file.writelines(func)
        file.write(self.two_empty_lines)
        return lines

    def list_view(self, a_list):
        return [(x + '\n') for x in a_list]
