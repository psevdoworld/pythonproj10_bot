import requests

def get_all_goods():
    res = requests.get('http://127.0.0.1:8000/shop/shop/')

    if res.status_code==200:
        return (res.json())

def like_by_id(good_id):
    print(f'http://127.0.0.1:8000/shop/shop/{good_id}/like/')
    res = requests.post(f'http://127.0.0.1:8000/shop/shop/{good_id}/like/')

    if res.status_code==200:
        return (res.json())