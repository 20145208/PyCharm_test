# @Time  : 2020/6/12 0012 22:48
# @Author: CaiYe
# @File  : remember_me.py

import json


def get_stored_username():
    filename = 'username1.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name?")
    filename = 'username1.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        checkname = input("Are you " + username + "?(YES/NO)")
        if checkname.lower() == 'yes':
            print("Welcome back, " + username + "!")
        elif checkname.lower() == 'no':
            get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("Please enter (yes/no) .")
            greet_user()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()