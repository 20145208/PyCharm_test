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


def main():
    # display_message('Jack', '996')
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

    print('')


main()