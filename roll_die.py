# @Time  : 2020/6/10 0010 4:47
# @Author: CaiYe
# @File  : roll_die.py

import random


class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        roll_die = random.randint(1, self.sides)
        print(roll_die)


die = Die()
die.roll_die()
die.sides = 10
die.roll_die()
die.sides = 20
die.roll_die()
