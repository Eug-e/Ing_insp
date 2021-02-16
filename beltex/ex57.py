import unittest
from unittest.mock import Mock
import example
# Найти в проекте вызов функций вида
# def fn1():
#     fn2()
# Если таких нет то написать
#  2. Написать тест для функции fn1 замокав вызов fn2
# def one (a, b):
#     c = a + b
#     return c
# # print(one(4,6))
#
# def two(x,y):
#     z = one(12, 8)
#     q = z + x + y
#     return q
# # print (two(1,2))

class Tests (unittest.TestCase):
    def test_two(self):
        example.one = Mock(return_value=15)

        self.assertTrue(example.two(4, 5) == 24)

if __name__ == '__main__':
    unittest.main()