# @Time  : 2020/6/11 0011 21:43
# @Author: CaiYe
# @File  : alice.py

filename = 'pg62357.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    print(contents.lower().count("planet"))