# @Time  : 2020/6/18 0018 21:33
# @Author: CaiYe
# @File  : employee.py


class Employee():
    def __init__(self, first_name, last_name, salary, middle_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name

    def give_raise(self, raise_salary=5000):
        self.salary = raise_salary + self.salary
        return self.salary
