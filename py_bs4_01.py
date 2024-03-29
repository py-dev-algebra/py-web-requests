import requests
from bs4 import BeautifulSoup


URL = 'https://www.worldometers.info/coronavirus/'
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

data = web_site_data.find_all('div', id="maincounter-wrap")

# print(data[0])
title = data[2].find('h1').get_text()
cases = data[2].find('span').get_text()
print(title, cases)
