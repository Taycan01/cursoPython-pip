import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    elementos = r.json()
    for ele in elementos:
        print(ele["name"])
        

get_categories()