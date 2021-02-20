import requests

def client():
    return requests.post(
        'http://127.0.0.1:8000/line18',
        {
            'id': 4,
            'name': "Hog",
            'age': 42
        }
    ).text
# print(client())

def client2():
    return requests.post(
        'http://127.0.0.1:8000/line19',
        {
            'id': 4
        }
    ).text
# print(client2())

