from django.test import TestCase
from .utils import two_numbers


class TwoNumbersTestCase(TestCase):
    def test_two_numbers(self):
        result = two_numbers(2, 3)
        self.assertEqual(result, 5)

