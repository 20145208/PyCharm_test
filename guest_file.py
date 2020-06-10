# @Time  : 2020/6/11 0011 6:30
# @Author: CaiYe
# @File  : guest_file.py


# filename = 'guest.txt'
# guest_name = input("Please enter your name:\n")
#
# with open(filename, 'a') as file_object:
#     file_object.write("guest's name: " + guest_name + "\n")

filename = 'guest_book.txt'
guest_name = ''
number_guest = 0

while True:
    guest_name = input("Please enter your name:(enter 'quit' to end) ")
    if guest_name == 'quit':
        break
    number_guest += 1
    with open(filename, 'a') as file_object:
        file_object.write("No." + str(number_guest) + ":" + str(guest_name) + "\n")
    print("Welcome!\n" + str(guest_name) + ",good day!")
