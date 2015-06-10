from unittest import TestCase

from generate_observations import _generate_studying_senz, _generate_working_senz, _generate_shopping_senz, _generate_dining_senz
from generate_observations import generate_studying_senz_list, generate_working_senz_list, generate_shopping_senz_list, generate_dining_senz_list
from generate_observations import _do_senz_map, map_senz

class TestBaseMethod(TestCase):

    def test_generate_studying_senz(self):
        _generate_studying_senz()

    def test_generate_working_senz(self):
        _generate_working_senz()

    def test_generate_shopping_senz(self):
        _generate_shopping_senz()

    def test_generate_dining_senz(self):
        _generate_dining_senz()


class TestInterfaceMethod(TestCase):

    def test_generate_studying_senz_list(self):
        result = generate_studying_senz_list(10, 1)
        self.assertEqual(1, len(result))
        self.assertEqual(10, len(result[0]))

    def test_generate_working_senz_list(self):
        result = generate_working_senz_list(10, 1)
        self.assertEqual(1, len(result))
        self.assertEqual(10, len(result[0]))

    def test_generate_shopping_senz_list(self):
        result = generate_shopping_senz_list(10, 1)
        self.assertEqual(1, len(result))
        self.assertEqual(10, len(result[0]))

    def test_generate_dining_senz_list(self):
        result = generate_dining_senz_list(10, 1)
        self.assertEqual(1, len(result))
        self.assertEqual(10, len(result[0]))


class TestMapMethod(TestCase):

    def test_do_senz_map(self):
        # case 1
        senz = {
            'motion': 'sitting',
            'sound': 'keyboard',
            'location': 'dining'
        }
        self.assertEqual(0, _do_senz_map(senz))

        # case 2
        senz = {
            'motion': 'sitting',
            'sound': 'bird',
            'location': 'dining'
        }
        self.assertEqual(5, _do_senz_map(senz))

    def test_map_senz(self):
        # case 1
        senz = {
            'motion': 'sitting',
            'sound': 'keyboard',
            'location': 'dining'
        }
        self.assertEqual([0], map_senz(senz))

        # case 2
        senz_list = [
            {
                'motion': 'sitting',
                'sound': 'keyboard',
                'location': 'dining'
            },
            {
                'motion': 'sitting',
                'sound': 'bird',
                'location': 'dining'
            }
        ]
        self.assertEqual([0,5], map_senz(senz_list))
