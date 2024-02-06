import requests

#region
# URL = 'https://www.algebra.hr/'

# response = requests.get(URL)

# print(f'Status Code: {response.status_code}')
# # print(f'Status Code: {response.content}')
# print(f'Headers: {response.headers}')
# print(f'Sadrzaj: {response.text}')
#endregion

URL = 'https://www.google.com/search?'
query = {
    'q': 'programiranje u pythonu'
}

response = requests.get(URL, params=query)

print(f'Status Code: {response.status_code}')
# print(f'Status Code: {response.content}')
print(f'Headers: {response.headers}')
print(f'Sadrzaj: {response.text}')
