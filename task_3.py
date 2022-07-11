""" 
Напишите программу, 
которая принимает на вход координаты точки 
(X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
номер четверти плоскости, в которой находится эта точка 
(или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 
"""

print('укажите координаты и мы скажем в какой четверти плоскости находится эта точка')
х_cord = int(input('укажите координаты X: '))
y_cord = int(input('укажите координаты Y: '))
if (х_cord > 0):
    if (y_cord > 0):
        print('Ваша точка находится в 1-ой плоскости координат')
    else:
        print('Ваша точка находится в 4-ой плоскости координат')
elif (х_cord < 0):
    if (y_cord < 0):
        print('Ваша точка находится в 3-ей плоскости координат')
    else:
        print('Ваша точка находится в 2-ой плоскости координат')
else:
    print('Ваша точка находится в пересечении плоскостей')