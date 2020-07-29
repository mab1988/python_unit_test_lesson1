from function.sort import bubble_sort
from unittest import TestCase

list = [2,0,1]
bubble_sort(list)
list2 = [3,6,8]
bubble_sort(list2)



class PlusFunctionTestCase(TestCase):
    def test_sort_list1(self):
        self.assertEqual([0, 1, 2], list)
    def test_sort_list2(self):
        self.assertEqual([8, 6, 2], list2)