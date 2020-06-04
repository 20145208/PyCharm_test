# @Time  : 2020/6/2 0002 0:26
# @Author: CaiYe
# @File  : dictionary.py


def months():
    # dateStr = input("Enter a date (mm/dd/yyyy):")
    # monthStr, dayStr, yearStr = dateStr.split("/")
    # months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    #           "November", "December"]
    # monthStr = months[int(monthStr) - 1]
    # print("The converted date is: ", monthStr, dayStr + ",", yearStr)
    #
    # dictionary_months = {
    #     '1': "January", '2': "February", '3': "March", '4':  "April",  '5': "May",  '6': "June",
    #     '7': "July",  '8': "August",  '9': "September",  '10': "October", '11': "November",  '12': "December",
    # }
    # print(dictionary_months['2'])
    # for i, j in dictionary_months.items():
    #     print('\nNumber: ' + i)
    #     print("Word: " + j)
    dictionary_namelike = {
        'kik': 'A6', 'pop': 'A6',
        'nan': 'B7', 'jaj': 'C5',
    }
    name_like = ['pop', 'jaj']
    for namelike in sorted(dictionary_namelike.keys()):
        print(namelike.title())
        if namelike in name_like:
            print("  Hi " + namelike.title() + "." + dictionary_namelike[namelike].title())
    print('\nbyb')


def alien_test0():
    # alien_0 = {'color': 'green', 'point': 5}
    alien_0 = {}
    alien_0['color'] = 'green'
    alien_0['points'] = 5
    print("the alien is " + alien_0['color'] + ".")
    alien_0['color'] = 'yellow'
    print("the alien is now " + alien_0['color'] + ".")
    # new_points = alien_0['point']
    print(alien_0)
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    alien_0['speed'] = 'medium'
    print(alien_0)
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3

    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print("New x-position: " + str(alien_0['x_position']))
    # print("You just earned " + str(new_points) + " points!")


def alien_test1():
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}

    aliens = [alien_0, alien_1, alien_2]

    for alien in aliens:
        print(alien)


def alien_test2():
    aliens = []
    for alien_number in range(5):
        new_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
        aliens.append(new_alien)
    for alien_number in range(50):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    for alien in aliens[:10]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

    for alien in aliens[:15]:
        print(alien)
    print('...')

    print("Total number of aliens: " + str(len(aliens)))


def many_users():
    users = {
        'cat': {
            'first': 'ada',
            'last': 'smith',
            'location': 'london',
        },

        'fish': {
            'first': 'bob',
            'last': 'white',
            'location': 'beijing',
        },
    }

    for username, user_info in users.items():
        print("\nUsername: " + username)
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']

        print("\tFull name: " + full_name.title())
        print("\tLocation: " + location.title())


def main():
    # months()
    # alien_test2()
    many_users()
    print(float(input(':')))


main()
