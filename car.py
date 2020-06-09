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

    def fill_gas_tank(self):
        print("Your tank is filled now!")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar("tesla", "model s", 2018)
print(my_tesla.get_descriptive_name())

my_new_car.odometer = 2223
my_new_car.update_odometer(11118)
my_new_car.increment_odometer(1222)

my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()