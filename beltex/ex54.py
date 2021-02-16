import threading
import time
import random


def api(result):
    time.sleep(3)
    result["key"] = random.randint(1, 100)

def first_exp():
    x = 0
    for i in range(5):
        s = {}
        api(s)
        x = s['key']+x
    print(x)
# first_exp()

def experiment():
    threads = []
    for i in range(5):
        result = {}
        t = threading.Thread(target=api, args=(result,))
        t.start()
        threads.append([t, result])
    thread_number = 1
    v = 0
    for thread, result in threads:
        thread.join()
        v = v + result['key']
        print("Поток " + str(thread_number) + ' вернул ' + str(result['key']))
        thread_number = thread_number + 1
    print(v)

if __name__ == "__main__":
    experiment()