import json
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as LH
import requests
from unidecode import unidecode
from io import StringIO


def get_content():
    reports = []
    with open('bigfoot_data.json') as f:
        for i in f:
            reports.append(json.loads(i))


    content_list = []
    data = pd.read_json('bigfoot_data.json', lines='true',orient='records')
    for i in range(len(reports)):
        soup = BeautifulSoup(reports[i]['html'], 'html.parser')

        tables = pd.read_html(data.iloc[i,1])
        content = tables[3][0][0]
        content = unidecode(content)
        content_list.append(content)

    return content_list


data = get_content()
