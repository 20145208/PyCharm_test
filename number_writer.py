# @Time  : 2020/6/11 0011 22:31
# @Author: CaiYe
# @File  : number_writer.py

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    print(json.load(f_obj))