# 1. Сделать генератор который принимает на вход число x, пусть x = 5, и возвращает 5 разных простых чисел.
# Простое число: число которое делится только на себя и на 1.
#
# Запустить генератор подав на вход 1 000 000, и сгенерировать с его помощью 6 простых чисел.
#
import random

def prime(x):
    if x in [0, 1]:
        return False
    if x == 2:
        return True
    for n in x.range(3, int(x ** 0.5 + 1)):
        if x % n == 0:
            return False
    return True
print(prime(random.randint(0, 1000)))

# def ex65(x):
#     ls = []
#     y = random.randint(0, 1000)
#
#     return ls
#
# print(ex65(5))
#
# 2. Превратить генератор в итератор
