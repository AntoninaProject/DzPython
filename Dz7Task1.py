#Создайте пользовательский аналог метода map().

from random import randint
def our map(func, matrix):
    return (func(el) for el in matrix)

def power (x):
    return x*x

nums =[1, 3, 12, 5]

print(list(our_map(power, nums)))