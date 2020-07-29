from function.plus_f import plus
from unittest import TestCase

def test_1_puls_1_return_2(self):
    self.assertEqual(2,plus(1, 1))

class PlusFunctionTestCase(TestCase):
    def test_1_puls_1_return_4(self):
        self.assertEqual(4,plus(2,2))

    def test_1_puls_1_return_5(self):
        self.assertEqual(5,plus(4,1))

    def test_1_puls_1_return_100(self):
        self.assertEqual(100,plus(20,80))