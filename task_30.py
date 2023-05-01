# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

start_number = int(input("Введите начальное число: "))
step = int(input("Введите шаг прогрессии: "))
quantity_numbers = int(input("Введите колличество элементов: "))
result=[]
result.append(start_number)
number =start_number
for i in range(1, quantity_numbers):
    number += step
    result.append(number)
print(result)