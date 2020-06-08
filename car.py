# @Time  : 2020/6/8 0008 22:20
# @Author: CaiYe
# @File  : car.py


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 110

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 2223
my_new_car.update_odometer(11118)
my_new_car.increment_odometer(1222)

my_new_car.read_odometer()