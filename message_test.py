# @Time  : 2020/6/4 0004 22:54
# @Author: CaiYe
# @File  : message_test.py


def display_message(user_name, user_id):
    print(user_name, user_id)


def make_album(singer_name, album_name, total_num=''):
    album = {'singer_name': singer_name, 'album_name': album_name, }
    if total_num:
       album['total_number'] = total_num

    return album


def do_album():
    while True:
        s_name = input("singer's name: ")
        if s_name == 'quit':
            break
        a_name = input("album's name: ")
        if a_name == 'quit':
            break
        t_number = input("How many songs?  ")
        if t_number == 'quit':
            break
        ablum_list = make_album(s_name, a_name, t_number)
        print("\n Information of albums:  ", ablum_list)


def greet_users(names):
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = 'the ' + unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


def do_models():
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    print_models(unprinted_designs[:], completed_models)
    show_completed_models(completed_models)
    print(unprinted_designs)


def main():
    # display_message('Jack', '996')
    # do_album()
    do_models()
    print('')


main()