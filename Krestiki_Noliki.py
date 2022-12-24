x, o = 'X', 'O'  # Создаем Двух пользователей
field = [('1', '2', '3',), ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # Поле для игры
coin = 0  # Счетчик ходов


def user(f, user, flag):  # Функция Игрока
    print(f'\nХодит {user}')
    for num, sp in enumerate(f):  # Отображаем поля для Игрока 1
        print(num, *sp)
    submit_field(user)
    victory(user, flag)


def submit_field(user):  # Проверка на свободную ячейку
    while True:
        stolbik = input('Введите цифру по столбик: ').strip()  # Запрашиваем у игрока число по горизонтали
        stolbik = submit_number(stolbik)  # Делаем проверку на правильность числа
        stroka = input('Введите цифру по строку: ').strip()  # Запрашиваем у игрока число по вертикали
        stroka = submit_number(stroka)
        if field[stroka][stolbik - 1] == '-':
            field[stroka][stolbik - 1] = user
            break
        print(f'\nЭто поле уже занято, поставьте в другом месте\n')


def submit_number(n):  # Функция проверки числа на int and 0 < int < 4
    while True:
        if n.isdigit():
            if 0 < int(n) < 4:
                return int(n)
        n = input('Введите число от 1 до 3: ')


def victory(user, flag):  # Функция победы
    # По горизонтали
    x1 = all([field[1][0] == x, field[1][1] == x, field[1][2] == x])
    x2 = all([field[2][0] == x, field[2][1] == x, field[2][2] == x])
    x3 = all([field[3][0] == x, field[3][1] == x, field[3][2] == x])

    # По вертикали
    y1 = all([field[1][0] == x, field[2][0] == x, field[3][0] == x])
    y2 = all([field[1][1] == x, field[2][1] == x, field[3][1] == x])
    y3 = all([field[1][2] == x, field[2][2] == x, field[3][2] == x])

    # По Диагонали
    xy1 = all([field[1][0] == x, field[2][1] == x, field[3][2] == x])
    xy2 = all([field[1][2] == x, field[2][1] == x, field[3][0] == x])

    if any([x1, x2, x3, y1, y2, y3, xy1, xy2]):
        print(f'Victory {user}')
        restart(flag)


def restart(flag):
    flag = input(
        '\nХотите сыграть еще раз?\nДля начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'
    return flag


# 1 День 1: понимание, что можно сделать через Декоратор, но надо ли?
# 2 День 2: Убрал 2 пользователя - сократил код. Добавил остановку и перезапуск на 9 ходу
#           Добавил проверку ячейки на занятость. Добавил условия победы


print(f'\nДобро пожаловать в игру "Крестики-Нолики\n\nДля игры нужно два человека\nВам нужно по очереди '
      f'вводитькоординаты ствоих фигур\n\n1 игрок = {x}\n2 игрок = {o}')
flag = input('Для начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'  # Начало/Конец игры

while flag:  # Запускаем бесконечный цикл
    user(field, x, flag)
    coin += 1
    if coin == 9:
        flag = restart(flag)
    user(field, o, flag)
    coin += 1
