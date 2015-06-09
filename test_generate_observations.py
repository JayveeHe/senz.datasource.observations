from unittest import TestCase

from generate_observations import _generate_studying_senz, _generate_working_senz, _generate_shopping_senz, _generate_dining_senz

class TestBaseMethod(TestCase):

    def test_generate_studying_senz(self):
        _generate_studying_senz()

    def test_generate_working_senz(self):
        _generate_working_senz()

    def test_generate_shopping_senz(self):
        _generate_shopping_senz()

    def test_generate_dining_senz(self):
        _generate_dining_senz()
