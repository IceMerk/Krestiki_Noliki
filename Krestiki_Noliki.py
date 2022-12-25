x, o = 'X', 'O'                                                                 # Создаем Двух пользователей
field = [('1', '2', '3',), ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]   # Поле для игры
coin = 0                                                                        # Счетчик ходов


def user(field, user):                  # Функция Игрока, передаем поле и нужного игрока
    print(f'\nХодит {user}')
    for num, sp in enumerate(field):    # Отображаем поля для игрока
        print(num, *sp)             # Выводим поле через enumerate
    submit_field(user)              # Проверяем поле на занятость
    if victory(field, user):        # Проверяем на победу
        return True
    return False

def submit_field(user):                                             # Проверка на свободную ячейку
    while True:
        stolbik = input('Введите цифру по столбик: ').strip()       # Запрашиваем у игрока число по горизонтали
        stolbik = submit_number(stolbik)                            # Проверка числа
        stroka = input('Введите цифру по строку: ').strip()         # Запрашиваем у игрока число по вертикали
        stroka = submit_number(stroka)                              # Проверка числа
        if field[stroka][stolbik - 1] == '-':                       # Сравниваем с символом в ячеке поля
            field[stroka][stolbik - 1] = user                       # Заменяем ячейку, если пустая
            break
        print(f'\nЭто поле уже занято, поставьте в другом месте\n') # Иначе говорим занято и по кругу


def submit_number(n):           # Функция проверки числа на int and 0 < int < 4
    while True:                 # Пока не введем верное значение, запрашиваем пользователя
        if n.isdigit():         # Если число в строке
            if 0 < int(n) < 4:  # Если число в диапозоне от 1 до 3 включительно
                return int(n)
        n = input('Введите число от 1 до 3: ')  # Иначе запрашиваем число и по кругу


def victory(field, user):  # Функция победы
    # По горизонтали
    x1 = all([field[1][0] == user, field[1][1] == user, field[1][2] == user])
    x2 = all([field[2][0] == user, field[2][1] == user, field[2][2] == user])
    x3 = all([field[3][0] == user, field[3][1] == user, field[3][2] == user])

    # По вертикали
    y1 = all([field[1][0] == user, field[2][0] == user, field[3][0] == user])
    y2 = all([field[1][1] == user, field[2][1] == user, field[3][1] == user])
    y3 = all([field[1][2] == user, field[2][2] == user, field[3][2] == user])

    # По Диагонали
    xy1 = all([field[1][0] == user, field[2][1] == user, field[3][2] == user])
    xy2 = all([field[1][2] == user, field[2][1] == user, field[3][0] == user])

    if any([x1, x2, x3, y1, y2, y3, xy1, xy2]):     # Если одно из условий верное, то победа
        print(f'\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Победили {user} ✧ﾟ･: *ヽ(◕ヮ◕ヽ)\n')
        for num, sp in enumerate(field):
            print(num, *sp)
        return True
    return False

def restart():  # Перезапуск/Завершение игры !!! Перезапуск: 3 глобальные изменяются flag, coin and field
    global flag
    flag = input(
        '\nХотите сыграть еще раз?\nДля начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'
    if flag:                    # Если игра продолжается, обнуляем поле и счетчик ходов
        global field
        field = [('1', '2', '3',), ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        global coin
        coin = 0
        return flag
    return flag             # Если игра заканчивается, возвращаем False и выходим


# 1 День 1: понимание, что можно сделать через Декоратор, но надо ли? (3ч)
# 2 День 2: Убрал 2 пользователя - сократил код. Добавил остановку и перезапуск на 9 ходу
#           Добавил проверку ячейки на занятость. Добавил условия победы. Добавил перезапуск игры (2.30ч)
# 3 День 3: Добавил проверку flag после каждого шага, поправил ошибки, добавил комментарии (3ч)
#           Посмотрел видео, решил переделать, только испортил и вернул обратно, после внес коректировки,
#           закрыл функции.


print(f'\nДобро пожаловать в игру "Крестики-Нолики\n\nДля игры нужно два человека\nВам нужно по очереди '
      f'вводитькоординаты ствоих фигур\n\n1 игрок = {x}\n2 игрок = {o}')
flag = input('Для начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'  # Начало/Конец игры

while flag:  # Запускаем бесконечный цикл
    if coin % 2 == 0:
        if user(field, x):
            restart()
    else:
        if user(field, o):
            restart()
    coin += 1
    if not flag:
        break
    if coin == 9:
        restart()
        if not flag:
            break
