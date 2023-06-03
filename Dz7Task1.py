#Создайте пользовательский аналог метода map().

from time import time
from random import randint
from os import system


def our_map(func, matrix):
    return (func(el) for el in matrix)


def power (x):
    return x*x


nums =[1, 3, 12, 5]

print(list(our_map(power, nums)))