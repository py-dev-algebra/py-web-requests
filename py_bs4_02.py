import requests
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com/catalogue/page-3.html'


response = requests.get(URL)
web_site_data = BeautifulSoup(response.content, 'html.parser')

#region
# all_paragraphs = web_site_data.find_all('p')
# all_anchors = web_site_data.find_all('a')
# all_headers1 = web_site_data.find_all('h1')
# all_headers3 = web_site_data.find_all('h3')
# for anchor in all_anchors:
#     print(anchor['href'])
#     print()
#endregion

data = web_site_data.find_all('article', _class="product_pod")
print(data)

# print(data[0])
#title = data[0].find('h3').get_text()
#cases = data[2].find('span').get_text()
#print(title)
