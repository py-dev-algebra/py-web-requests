import urllib.request
import urllib.parse


# Upit prema serveru GET - gohvat podataka
URL = 'https://www.algebra.hr/'
request = urllib.request.urlopen(url=URL)
web_content = request.read().decode()

# print(web_content)





# Upit prema serveru POST - dohvat podataka - DICT!!! - bio string
query = {}
users_quesry = input('Upisite tekst pretrage na Google.com: ')
# query = {
#     'q': 'programiranje u pythonu'
# }
query['q'] = users_quesry

encoded_query = urllib.parse.urlencode(query).encode('utf-8')
URL_REQUEST = f'https://www.google.com/search?{encoded_query}'

request = urllib.request.urlopen(URL_REQUEST)
response = request.read().decode()

print(response)
