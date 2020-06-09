# @Time  : 2020/6/10 0010 3:57
# @Author: CaiYe
# @File  : user_class.py

class User():
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print("User info: " + self.first_name + ' ' + self.last_name + " from " + self.country + '.')

    def greet_user(self):
        print("Hi!Welcome! Dear " + self.first_name + ' ' + self.last_name + '.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


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


user1 = User('Cai', 'Ye', 'China')
user2 = User('Seth', 'White', 'England')
user3 = User('Lucy', 'Smith', 'American')

user1.describe_user()
user2.greet_user()
print(user3.login_attempts)
print(user3.increment_login_attempts())
print(user3.increment_login_attempts())
print(user3.reset_login_attempts())

admin1 = Admin('admin', '1', 'none')
admin1.privileges.show_privileges()