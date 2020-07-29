from function.gcd import gcd
from unittest import TestCase


class PlusFunctionTestCase(TestCase):
    def test1_gcd_30_10(self):
        self.assertEqual(10,gcd(30,10))

    def test1_gcd_20_1(self):
        self.assertEqual(10, gcd(20, 1))