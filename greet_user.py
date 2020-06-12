# @Time  : 2020/6/11 0011 22:46
# @Author: CaiYe
# @File  : greet_user.py
import json

filename = 'users_name1.json'
username = input("What's your name?")

try:
    with open(filename) as f_obj:
        users_name = json.load(f_obj)

except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        # new_user = {username: 'guest'}
        # json.dump(new_user, f_obj)
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

else:
    # if username in users_name.keys():
    #     print("Welcome back, " + username + "!")
    # elif username not in users_name.keys():
    #     with open(filename, 'w') as f_obj:
    #         users_name[username] = 'guest'
    #         json.dump(users_name, f_obj)
    #         print("We'll remember you when you come back, " + username + "!")
    if username in users_name:
        print("Welcome back, " + username + "!")
    elif username not in users_name:
        with open(filename, 'w') as f_obj:
            users_name = username + "," + users_name
            json.dump(users_name, f_obj)
            print("We'll remember you when you come back, " + username + "!")



print(' ')