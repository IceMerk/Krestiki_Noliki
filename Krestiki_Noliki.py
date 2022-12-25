x, o = 'X', 'O'  # Создаем Двух пользователей
field = [('1', '2', '3',), ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # Поле для игры
coin = 0  # Счетчик ходов


def user(f, user):  # Функция Игрока, передаем поле и нужного игрока
    print(f'\nХодит {user}')
    for num, sp in enumerate(f):  # Отображаем поля для игрока
        print(num, *sp)  # Выводим поле через enumerate
    submit_field(user)  # Проверяем поле на занятость
    victory(f, user)  # Проверяем на победу


def submit_field(user):  # Проверка на свободную ячейку
    while True:
        stolbik = input('Введите цифру по столбик: ').strip()  # Запрашиваем у игрока число по горизонтали
        stolbik = submit_number(stolbik)  # Проверка числа
        stroka = input('Введите цифру по строку: ').strip()  # Запрашиваем у игрока число по вертикали
        stroka = submit_number(stroka)  # Проверка числа
        if field[stroka][stolbik - 1] == '-':  # Сравниваем с символом в ячеке поля
            field[stroka][stolbik - 1] = user  # Заменяем ячейку, если пустая
            break
        print(f'\nЭто поле уже занято, поставьте в другом месте\n')  # Иначе говорим занято и по кругу


def submit_number(n):  # Функция проверки числа на int and 0 < int < 4
    while True:  # Пока не введем верное значение, запрашиваем пользователя
        if n.isdigit():  # Если число в строке
            if 0 < int(n) < 4:  # Если число в диапозоне от 1 до 3 включительно
                return int(n)
        n = input('Введите число от 1 до 3: ')  # Иначе запрашиваем число и по кругу


def victory(field, user):
    def message_viktory():  # Сообщение о победе
        print(f'\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Победили {user} ✧ﾟ･: *ヽ(◕ヮ◕ヽ)\n')
        for num, sp in enumerate(field):
            print(num, *sp)
        restart()

    def check_line(a, b, c, user):  # Проверка на правильность поля символу игрока
        if a == user and b == user and c == user:
            message_viktory()
            flag = False
            return flag

    for i in range(1, 4):  # Горизонталь + диагональ
        if check_line(field[i][0], field[i][1], field[i][2], user) or \
                check_line(field[1][0], field[2][1], field[3][2], user) or \
                check_line(field[1][2], field[2][1], field[3][0], user):
            break

    for i in range(3):  # Вертикаль
        if check_line(field[1][i], field[2][i], field[3][i], user):
            break


def restart():  # Перезапуск/Завершение игры !!! Перезапуск: 3 глобальные изменяются flag, coin and field
    global flag
    flag = input(
        '\nХотите сыграть еще раз?\nДля начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'
    if flag:  # Если игра продолжается, обнуляем поле и счетчик ходов
        global field
        field = [('1', '2', '3',), ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        global coin
        coin = 0
    else:
        return flag  # Если игра заканчивается, возвращаем False и выходим


# 1 День 1: понимание, что можно сделать через Декоратор, но надо ли? (3ч)
# 2 День 2: Убрал 2 пользователя - сократил код. Добавил остановку и перезапуск на 9 ходу
#           Добавил проверку ячейки на занятость. Добавил условия победы. Добавил перезапуск игры (2.30ч)
# 3 День 3: Добавил проверку flag после каждого шага, поправил ошибки, добавил комментарии (2ч)


print(f'\nДобро пожаловать в игру "Крестики-Нолики\n\nДля игры нужно два человека\nВам нужно по очереди '
      f'вводитькоординаты ствоих фигур\n\n1 игрок = {x}\n2 игрок = {o}')
flag = input('Для начала игры нажмите Y, чтобы закончить - любую клавишу: ').lower() == 'y'  # Начало/Конец игры

while flag:  # Запускаем бесконечный цикл
    if coin % 2 == 0:
        user(field, x)
    else:
        user(field, o)
    coin += 1
    if not flag:
        break
    if coin == 9:
        restart()
        if not flag:
            break
