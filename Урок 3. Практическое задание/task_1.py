"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def divide(arg1, arg2):
    try:
        result = arg1 / arg2
        print(result)
    except ZeroDivisionError:
        print("нельзя делить на ноль!")


divide(arg1=int(input('Введите делимое число - ')), arg2=int(input('Введите делитель - ')))
