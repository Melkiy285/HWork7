first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))

if first == second and first == third:
    print('Все', 3, 'числа равны между собой')
elif first == second or first == third or second == third:
    print(2, 'числа равны между собой')
else:
    print('Обнаружено', 0, 'равных между собой чисел')