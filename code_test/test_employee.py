# @Time  : 2020/6/18 0018 21:38
# @Author: CaiYe
# @File  : test_employee.py


import unittest
from code_test.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee('Bob', 'Smith', 6000)

    def test_give_default_raise(self):
        self.assertEqual(self.test_employee.salary + 5000, self.test_employee.give_raise())

    def test_give_custom_raise(self):
        custom_raise = 6000
        self.assertEqual(self.test_employee.salary + custom_raise, self.test_employee.give_raise(custom_raise))