import threading
import time
import random

def fn(result, a):
    print('fn начала исполняться с аргументом: ' + str(a))
    time.sleep(2)
    result['result'] = a + 5

def experiment():
    threads = []
    for i in range(2):
        result = {}
        t = threading.Thread(target=fn, args=(result, random.randint(1, 100)))
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, result in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(result['result']))
        thread_number = thread_number + 1

if __name__ == "__main__":
    experiment()
