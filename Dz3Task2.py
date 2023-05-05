#В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
#а –> абрикос, авокадо, апельсин, айва.

fruits_list = "Яблоко Абрикос Авокадо Банан Инжир Ежевика Финики Крыжовник"
fruits_list = fruits_list.split(" ")
print(fruits_list)

letter = input('Введите букву: ').lower()

for fruit in fruits_list:
    if letter == fruit[0].lower():
        print(fruit) 