from function.email import is_correct_email
from unittest import TestCase


class PlusFunctionTestCase(TestCase):
    def test1_email_correct(self):
        self.assertTrue(is_correct_email("mir@mail.ru"))

    def test1_email2_no_signs(self):
        self.assertTrue(is_correct_email("mirmailru"))

    def test1_email3_only_Numbers(self):
        self.assertTrue(is_correct_email("m097766"))