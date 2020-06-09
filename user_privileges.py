# @Time  : 2020/6/10 0010 4:35
# @Author: CaiYe
# @File  : user_privileges.py


from user_class import User


class Admin(User):
    def __init__(self, first_name, last_name, country):
        super().__init__(first_name, last_name, country)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("You can do these:" + str(self.privileges))
