# -*- encoding: utf-8 -*-

########################################
# Here you have a way to define a class 
# without going through that round trip 
# of using class keyword
########################################

from collections import namedtuple

Car = namedtuple('Car', 'color mileage brand model')

my_car = Car('red', '3.1234', 'Toyota', 'S3')

print(f"My car is {my_car.brand} {my_car.model} with mileage {my_car.mileage} and is {my_car.color} in color.")
