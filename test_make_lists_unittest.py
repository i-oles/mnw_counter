import unittest
from PyQt5.QtWidgets import QMainWindow
from main import IzzyCounterWindow

# todo fix test

class TestMakeItemsList(unittest.TestCase):
    def setUp(self):
        self.configs = IzzyCounterWindow(QMainWindow)

        self.ones_all = ['szm123_1mnw(1).tiff',
                         'szm123_2mnw(1).tiff',
                         'szm123_1-2mnw(1).tiff',
                         'szm111_a-cmnw!a(1).tiff',
                         'szm111_a-cmnw!b(1).tiff',
                         'szm111_a-cmnw(1).tiff'
                         ]

    def test_make_singles_and_set_list(self):
        self.configs.make_singles_and_set_list()

        self.result_single = ['szm123_1', 'szm123_2', 'szm111_a-c']

        self.assertEqual(self.ones_all, self.result_single)


if __name__ == '__main__':
    unittest.main()
