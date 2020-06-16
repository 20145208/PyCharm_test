# @Time  : 2020/6/16 0016 23:02
# @Author: CaiYe
# @File  : area.py

from code_test.const import PI


def calc_round_area(radius):
    return PI * (radius ** 2)


def main():
    print('1:', calc_round_area(2))


main()
