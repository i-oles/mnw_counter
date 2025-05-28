import re
import os


class MNWProvider:
    def __init__(self, dir_path, file_ext):
        self.dir_path = dir_path
        self.file_ext = file_ext
        self.object_separator = ","
        self.mnw_prefix = "mnw"

    def provide_objects_lists(self) -> (list, list):
        signatures = self.get_objects_signatures()
        signatures_single, signatures_set = separate_sets_and_singles(signatures)

        return signatures_single, signatures_set

    # get all unique signatures from filenames ended with '(1)' from provided directory
    # filenames can contain two object signatures - that's why we split by given separator
    def get_objects_signatures(self):
        signatures_with_prefix = []
        search_pattern = rf'.*\(0?0?0?1\)\.{self.file_ext}?$'
        for _, _, filenames in os.walk(self.dir_path):
            for filename in filenames:
                if re.findall(r'{}'.format(search_pattern), filename):
                    signatures_with_prefix += filename.split(self.object_separator)

        signatures = []

        for signature in signatures_with_prefix:
            if self.mnw_prefix in signature:
                index = signature.find(self.mnw_prefix)
                signatures.append(signature[:index])

        return sorted(set(signatures))


def separate_sets_and_singles(signatures: list) -> (list, list):
    signatures_set = []

    for signature in signatures:
        if re.search(r'\d-\d', signature):
            signatures_set.append(signature)
            signatures.remove(signature)

    return sorted(set(signatures)), sorted(set(signatures_set))
