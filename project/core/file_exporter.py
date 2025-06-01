import os
from abc import ABC, abstractmethod
from datetime import date

REPORT_DIR_NAME = "daily_reports"


class FileExporter(ABC):
    def __init__(
        self,
        dir_path: str,
        total_count: int,
        signatures_single: list[str],
        signatures_set: list[str],
    ) -> None:
        self.dir_path = dir_path
        self.total_count = (total_count,)
        self.signatures_single = (signatures_single,)
        self.signatures_set = signatures_set

    @abstractmethod
    def generate_report(self) -> None:
        pass


class DailyReportFileExporter(FileExporter):
    def __init__(
        self,
        dir_path: str,
        total_count: int,
        signatures_single: list[str],
        signatures_set: list[str],
    ) -> None:
        super().__init__(dir_path, total_count, signatures_single, signatures_set)
        self.report_dir_path = os.path.join(dir_path, REPORT_DIR_NAME)
        self.total_count = total_count
        self.signatures_single = signatures_single
        self.signatures_set = signatures_set

    def generate_report(self) -> None:
        current_date = date.today().strftime("%d-%m-%Y")
        os.makedirs(self.report_dir_path, exist_ok=True)
        report_path = os.path.join(self.report_dir_path, f"{current_date}.txt")

        with open(report_path, "w", encoding="utf-8") as file:
            file.write(f"Date: {current_date}\n\n")
            file.write(f"You had taken pictures of {self.total_count} objects.\n\n")
            file.write("Photographed:\n")
            file.writelines(list_view(self.signatures_single))
            file.write("\n")

            if self.signatures_set:
                file.write("Additional images contain objects in sets:\n")
                file.writelines(list_view(self.signatures_set))
                file.write("\n")


def list_view(some_list: list[str]) -> list[str]:
    return [f"{line}\n" for line in some_list]
