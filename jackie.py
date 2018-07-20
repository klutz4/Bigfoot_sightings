import json
from bs4 import BeautifulSoup

import json

reports = []
with open('bigfoot_data.json') as f:
    for i in f:
        reports.append(json.loads(i))


#reports[0]

#print(reports[0].keys(), '\n')

# for k, v in reports[0].items():
#     print(f'{k}: {v} \n')

soup = BeautifulSoup(reports[0]['html'], 'html.parser')

# print(soup.prettify())
#
# print(soup.title)
# print(soup.title.text)
#
# soup.get_text()

# soup.find_all('span')
