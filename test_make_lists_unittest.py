#import unittest
#from main import IzzyCounterWindow
import os

"""
class TestMakeLists(unittest.TestCase):
    def test_make_lists(self):
        self.files_for_test = ['szm123_1mnw(1).tiff',
                               'szm123_2mnw(1).tiff',
                               'szm123_1-2mnw(1).tiff',
                               'szm111_a-cmnw!a(1).tiff',
                               'szm111_a-cmnw!b(1).tiff',
                               'szm111_a-cmnw(1).tiff'
                               ]

        self.result_single = ['szm123_1', 'szm123_2', 'szm111_a-c']

        self.assertEqual(IzzyCounterWindow.make_singles_and_set_list(self.files_for_test, self.result_single))



class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

"""

dir = '/Users/ioles/Desktop/'

if os.path.isfile(dir):
    print('')

if __name__ == '__main__':
    pass