from unittest import TestCase

from generate_observations import _generate_studying_senz, _generate_working_senz, _generate_shopping_senz, _generate_dining_senz
from generate_observations import generate_studying_senz_list, generate_working_senz_list, generate_shopping_senz_list, generate_dining_senz_list

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
