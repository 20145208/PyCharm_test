# @Time  : 2020/6/10 0010 4:26
# @Author: CaiYe
# @File  : my_car.py

from car import Car, ElectricCar

my_new_car = Car('audi', 'a7', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer = 23333
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print("\n" + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()