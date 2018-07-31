import json
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as LH
import requests
from io import StringIO


import json

reports = []
with open('bigfoot_data.json') as f:
    for i in f:
        reports.append(json.loads(i))


content_list = []
data = pd.read_json('bigfoot_data.json', lines='true',orient='records')
for i in range(len(reports)):
    soup = BeautifulSoup(reports[i]['html'], 'html.parser')

    '''

    data = []
    table = soup.find('span', attrs={'class':'reportclassification'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    '''

    #soup = BeautifulSoup(data['html'])

    tables = pd.read_html(data.iloc[i,1])
    content = tables[3][0][0]
    content_list.append(content)




# for k, v in reports[0].items():
#     print(f'{k}: {v} \n')

soup = BeautifulSoup(reports[0]['html'], 'html.parser')

#
# print(soup.title)
# print(soup.title.text)
#
#print(soup.get_text())
#print(table)
#data = pd.read_html(table)
