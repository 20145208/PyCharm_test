# @Time  : 2020/6/16 0016 21:30
# @Author: CaiYe
# @File  : test_name_function.py

import unittest
from code_test.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('cai', 'ye', ' 1')
        self.assertEqual(formatted_name, 'Cai Ye')


# print("**** "+__name__)
if __name__ == '__main__':
    unittest.main()


# unittest.main()