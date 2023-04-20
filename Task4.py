# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
#5 -> 2, 4
#8 -> 2, 4, 6, 8

start = int(input("Введите начальное число диапазона: "))
end = int(input("ВВедите итоговое число диапазона: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")