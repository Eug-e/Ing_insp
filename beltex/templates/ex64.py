# 1. Написать функцию которая будет распаковывать цифры 7 и 6 в переменные x и y из списка
# ls = [4,[7,8],6] Использовать unboxing.
def one():
    ls = [4,[7,8],6]
    x,y,z = ls
    return y[0], z
print(one())


# 2. Написать функцию которая будет бежать for-ом по списку  ls = [ (3, [9, 1]), [(23,43), [5, 4]] ]
# и суммировать элементы 9 и 5 используя unboxing.
def two():
    ds = []
    ls = [(3, [9, 1]), [(23, 43), [5, 4]]]
    for x, (y, z) in ls:
        ds.append(y)
    return ds[0]+ds[1]
print (two())