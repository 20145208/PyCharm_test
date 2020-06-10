# @Time  : 2020/6/11 0011 6:23
# @Author: CaiYe
# @File  : write_message.py


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I want to sleep!\n")
    file_object.write("I hate work in night = =.\n")