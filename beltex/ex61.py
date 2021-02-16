from datetime import datetime
import random

def first():
    ls = []
    for _ in range(2000000):
        ls.append(random.randint(1, 10**5))

    start = datetime.now()
    for _ in range(100):
        random.randint(1, 10**5) in ls
    print('1. 100 раз в списке за ' + str((datetime.now() - start).total_seconds()) + ' сек')

    hash = set(ls)
    start = datetime.now()

    for _ in range(100):
        random.randint(1, 10**5) in hash
    print('2. 100 раз в множестве за ' + str((datetime.now() - start).total_seconds()) + ' сек')
first()