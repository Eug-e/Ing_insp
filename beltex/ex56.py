import unittest


# 1. Написать функцию которая находит общие элементы из 2-х списков. Написать для неё тесты.
def test_one (ls, ds):
    x = []
    for i in ls:
        if i in ds:
            x.append(i)
    return x
# print(test_one([2,8,9,16,78,499], [78,46,9,16,49]))

# class Tests (unittest.TestCase):
#     def test_test_one(self):
#         result = test_one([2,6,8,4], [2,8,9])
#         self.assertTrue(result == [2,8])
#
# if __name__ == '__main__':
#     unittest.main()

# 2. Написать функцию которая удаляет дубли в списках.  Написать для неё тесты.
def test_two (ls):
    x = []
    for i in ls:
        if i not in x:
            x.append(i)
    return x

print(test_two([2, 8, 9, 16, 78, 499, 16, 8]))


class Tests (unittest.TestCase):
    def test_test_two(self):
        result = test_two([2,6,8,4,2,8])
        self.assertTrue(result == [2,6,8,4])

if __name__ == '__main__':
    unittest.main()