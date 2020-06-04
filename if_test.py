# @Time  : 2020/6/2 0002 21:38
# @Author: CaiYe
# @File  : if_test.py


def age():
    age = int(input('Please enter your age:'))
    if age < 2:
        print("Baby.")
    elif 2 <= age < 4:
        print("Big baby.")
    elif 4 <= age <13:
        print("Child")
    elif 13 <= age <20:
        print("Teen")
    elif 20 <= age <65:
        print("Adult")
    elif age >= 65:
        print("You are old man!")


def toppings():
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = input("What kind of pizza would you like?(use ',' between each one)\n").split(',')
    #requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
                print("Adding " + requested_topping + ".")
        else:
            print("Sorry,we don't have " + requested_topping + ".")

    print("\nFinished making your pizza!")


def say_hello():
    user_names = ['admin', 'ada', 'bob', 'candy', 'erect', 'fool']
    new_users = ['hill', 'idea', 'jack', 'ken', 'FOOL', 'fool']

    for new_user in new_users:
        if new_user.lower() in [i.lower() for i in user_names]:
            print("You need to change another name")
        else:
            print("You can use the name")
    if user_names:
        for user_name in user_names:
            if user_name == 'admin':
                print("Hello admin,would you like to see a status report?")
            else:
                print("Hello " + user_name + ",good day!")
    else:
        print("We need some users")
    for number in range(1, 10):
        if number == 1:
            print(str(number) + "st")
        elif number == 2:
            print(str(number) + "nd")
        elif number == 3:
            print(str(number) + "rd")
        else:
            print(str(number) + "th")


def alien(color):
    alien_color = color
    if alien_color == 'green':
        print('get 5 points!')
    elif alien_color == 'yellow':
        print('get 10 points!')
    elif alien_color == 'red':
        print('get 15 points!')


def main():
    # age()
    # toppings()
    # alien('red')
    say_hello()

main()