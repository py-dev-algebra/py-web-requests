import requests
import json

URL_BASE = 'https://jsonplaceholder.typicode.com'
URL_USERS_EXTENSION = '/users/5'
URL_POSTS_EXTENSION = '/post'

response = requests.get(f'{URL_BASE}{URL_USERS_EXTENSION}')

if response.status_code == 200:
    data = response.json()
    print(data['name'])

    # for key, value in data.items():
    #     print(key, value)

    # data_str = json.dumps(data, indent=4)
    # print(data_str)
else:
    print(f'dogodila se greska: {response.status_code}')
