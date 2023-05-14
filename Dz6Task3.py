# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

from random import randint
def task3():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    drobi = []
    for i in range(1, 11):
        zn = []
        for j in range(i + 1, 12):
            if gcd(j, i) == 1:
                zn.append(f"{i}/{j}")
        drobi.append(zn)

    for zn in drobi:
        print(zn)