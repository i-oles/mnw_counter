import os
import re
from abc import ABC, abstractmethod


class Provider(ABC):
    def __init__(self, dir_path: str, file_ext: str) -> None:
        self.dir_path = dir_path
        self.file_ext = file_ext

    @abstractmethod
    def provide_objects_lists(self) -> (list[str], list[str]):
        pass


class MNWProvider(Provider):
    def __init__(self, dir_path: str, file_ext: str) -> None:
        super().__init__(dir_path, file_ext)
        self.dir_path = dir_path
        self.file_ext = file_ext
        self.object_separator = ","
        self.mnw_prefix = "mnw"

    def provide_objects_lists(self) -> (list[str], list[str]):
        signatures = get_objects_signatures(
            self.dir_path,
            self.file_ext,
            self.object_separator,
            self.mnw_prefix,
        )
        signatures_single, signatures_set = separate_sets_and_singles(signatures)

        return signatures_single, signatures_set


# get all unique signatures from filenames ended with '(1)' from provided directory
# filenames can contain two object signatures - it's needed to split by separator
def get_objects_signatures(
    dir_path: str,
    file_ext: str,
    object_separator: str,
    prefix: str,
) -> list[str]:
    signatures_with_prefix = []
    search_pattern = rf".*\(0?0?0?1\)\.{file_ext}?$"
    for _, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if re.findall(rf"{search_pattern}", filename):
                signatures_with_prefix += filename.split(object_separator)

    signatures = []

    for signature in signatures_with_prefix:
        if prefix in signature:
            index = signature.find(prefix)
            signatures.append(signature[:index])

    return sorted(set(signatures))


def separate_sets_and_singles(signatures: list[str]) -> (list[str], list[str]):
    signatures_set = []
    signatures_single = []

    for signature in signatures:
        if re.search(r"\d-\d", signature):
            signatures_set.append(signature)
        else:
            signatures_single.append(signature)

    return sorted(set(signatures_single)), sorted(set(signatures_set))
