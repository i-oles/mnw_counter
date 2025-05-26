from datetime import date
import os

REPORT_DIR_NAME = 'daily_reports'

def make_dir_if_not_exist(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def list_view(some_list):
    return [f'{line}\n' for line in some_list]

class ExportToFile:
    def __init__(self, dir_path, count_result, singles_list, sets_list=None):
        self.count_result = count_result
        self.singles_list = singles_list
        self.sets_list = sets_list or []
        self.current_date = date.today().strftime("%d-%m-%Y")
        self.report_dir_path = os.path.join(dir_path, REPORT_DIR_NAME)

    def generate_report(self):
        make_dir_if_not_exist(self.report_dir_path)
        report_path = os.path.join(self.report_dir_path, f'{self.current_date}.txt')

        with open(report_path, 'w', encoding='utf-8') as file:
            file.write(f'Date: {self.current_date}\n\n')
            file.write(f'You had taken pictures of {self.count_result} objects.\n\n')
            file.write('Photographed:\n')
            file.writelines(list_view(self.singles_list))
            file.write('\n')

            if self.sets_list:
                file.write('Additional images contain objects in sets:\n')
                file.writelines(list_view(self.sets_list))
                file.write('\n')
