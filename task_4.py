""" 
Напишите программу, 
которая по заданному номеру четверти, 
показывает диапазон возможных координат 
точек в этой четверти (x и y). 
"""



number = int(input('Введите размер вашей плоскости в точках: '))
number_quater = int(input('Введите номер четверти (от 1 до 4) чтобы узнать диапозон возможных точек: '))

if  number_quater == 1 or number_quater == 2:
    print('Диапозон возможных точек координат по Х: от 0 до ',number)

elif number_quater == 3 or number_quater == 4:

    print('Диапозон возможных точек координат по Х: от 0 до ',-number)

if number_quater == 1 or number_quater == 4:

    print('Диапозон возможных точек координат по Y: от 0 до ',number)

elif number_quater == 2 or number_quater == 3:

    print('Диапозон возможных точек координат по Y: от 0 до ',-number)

else:
    print('Стоило ввести корректный номер четверти (от 1 до 4)')