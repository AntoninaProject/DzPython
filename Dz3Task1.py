#Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
#6 –> 1 1 2 3 5 8

num = [0, 1]

count = 15

for i in range(2, count):
    num.append(num[i-2] + num[i-1])
print(num)