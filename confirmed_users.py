# @Time  : 2020/6/4 0004 22:10
# @Author: CaiYe
# @File  : confirmed_users.py


def con_users():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    while unconfirmed_users:
        current_users = unconfirmed_users.pop()

        print("Verifying user: " + current_users.title())
        confirmed_users.append(current_users)

    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


def pets_name():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')

    print(pets)


def mountain_poll():
    responses = {}
    polling_active = True
    while polling_active:
        name = input("\nWhat is your name? \nYour name: ")
        response = input("Which mountain would you like to climb someday? \nMountain's name: ")
        responses[name] = response
        repeat = input("Would you like to let another person respond?(yes/no): ")
        if repeat.lower() == 'no':
            polling_active = False

    print("\n<<<---Poll Results--->>>")
    for name, response in responses.items():
        print(name.title() + " would like to climb " + response.title() + ".")


def sandwich_store():
    sandwich_orders = ['Big Bar', 'Medium Boy', 'Little Bus', 'pastrami', 'pastrami', 'pastrami']
    finished_sandwich = []
    print('Pastrami was sale out!')

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while sandwich_orders:
        new_finished = sandwich_orders.pop()
        print('I made your tuna sandwich,' + new_finished)

        finished_sandwich.append(new_finished)

    print("All of the finished sandwiches: " + str(finished_sandwich))


def main():
    # con_users()
    # pets_name()
    # mountain_poll()
    sandwich_store()
    print('')


main()