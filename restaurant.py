# @Time  : 2020/6/9 0009 22:39
# @Author: CaiYe
# @File  : restaurant.py

class Restaurant():
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def set_number_served(self, numbers):
        self.number_served = numbers

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

    def describe_restaurant(self):
        print("The restaurant is a " + self.restaurant_type + " restaurant and named " + self.restaurant_name + " .")

    def open_restaurant(self):
        print("This restaurant is opening.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type):
        self.flavors = ['green tea', 'red been', 'gold cream']

    def describe_flavors(self):
        print("We have " + str(self.flavors).replace('[', '').replace(']', '').replace(',', ' '))


my_restaurant = Restaurant("Big Big", "ice-cream")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_icecream_restaurant = IceCreamStand("BIG ICE", "ice cream")
my_icecream_restaurant.describe_flavors()

print(my_restaurant.number_served)
my_restaurant.set_number_served(5)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(11)
print(my_restaurant.number_served)