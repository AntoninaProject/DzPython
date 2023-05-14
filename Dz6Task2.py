# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, 
# которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.

from random import randint

def task2(n):
    def digList(num):
        if num == 0:
            return [0]
        digits = []
        while num != 0:
            digits.insert(0, num % 10)
            num //= 10
        return digits

    lst = [randint(0, 9) for i in range(15)]
    digsn = digList(n)
    lenLst = len(lst)
    lenDigsn = len(digsn)
    print(lst)
    print(n)
    stop = lenLst - lenDigsn + 1
    i = 0
    while i < stop:
        if lst[i:i + lenDigsn] == digsn:
            print("Да")
            break
        i += 1
    else:
        print("Нет")
