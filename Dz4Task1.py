#Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и 
#количество этих множителей.
#60 -> 2, 2, 3, 5

num = 131
div = 2
dividers = []
while num != 1:
    if num % div == 0:
        dividers.append(div)
        num//=div
    else:
        div+-1
print(dividers)
print(f'количество простых множителей {len(dividers)}')
    