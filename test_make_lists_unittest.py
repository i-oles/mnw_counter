import unittest
from main import IzzyCounterWindow

class TestMakeItemsList(unittest.TestCase):
    IzzyCounterWindow.ones_all = ['szm123_1mnw(1).tiff',
                                  'szm123_2mnw(1).tiff',
                                  'szm123_1-2mnw(1).tiff',
                                  'szm123_a-bmnw(1).tiff',
                                  'szm123_a-bmnw!a(1).tiff',
                                  'szm123_1mmw(1).tiff',
                                  'szm123_111(1).tiff']

    IzzyCounterWindow.coma_char = ','
    IzzyCounterWindow.component = 'mnw'
    IzzyCounterWindow.hyphen_char = '-'

    def test_make_singles_and_set_list(self):
        actual_result = IzzyCounterWindow.make_singles_and_set_list(IzzyCounterWindow)
        expected_result = ['szm123_1', 'szm123_2', 'szm123_a-b'], ['szm123_1-2']

        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
