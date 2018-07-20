import json
from bs4 import BeautifulSoup

import json

reports = []
with open('bigfoot_data.json') as f:
    for i in f:
        reports.append(json.loads(i))

mega = []
for i in range(len(reports)):
    soup = BeautifulSoup(reports[i]['html'], 'html.parser')

    html = soup.get_text()
    # headers = ['YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION DETAILS', 'NEAREST TOWN', 'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED', 'OTHER WITNESSES', 'OTHER STORIES', 'TIME AND CONDITIONS', 'ENVIRONMENT']
    with open('html.csv', "w") as outfile:
        for entries in html[html.find('YEAR'):html.find('SEASON')]:
            outfile.write(entries)
        for entries in html[html.find('SEASON'):html.find('MONTH')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('MONTH'):html.find('STATE')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('STATE'):html.find('COUNTY')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('COUNTY'):html.find('LOCATION DETAILS')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('LOCATION DETAILS'):html.find('NEAREST TOWN')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('NEAREST TOWN'):html.find('NEAREST ROAD')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('NEAREST ROAD'):html.find('OBSERVED')]:
            outfile.write(entries)
        outfile.write('\n')
        for entries in html[html.find('OBSERVED'):html.find('ALSO NOTICED')]:
            outfile.write(entries)
        # outfile.write('\n')
        # for entries in html[html.find('ALSO NOTICED'):html.find('OTHER WITNESSES')]:
        #     outfile.write(entries)
        # outfile.write('\n')
        # for entries in html[html.find('OTHER WITNESSES'):html.find('OTHER STORIES')]:
        #     outfile.write(entries)
        # outfile.write('\n')
        # for entries in html[html.find('OTHER STORIES'):html.find('TIME AND CONDITIONS')]:
        #     outfile.write(entries)
        # outfile.write('\n')
        # for entries in html[html.find('TIME AND CONDITIONS'): html.find('ENVIRONMENT')]:
        #     outfile.write(entries)
        # outfile.write('\n')
        # for entries in html[html.find('ENVIRONMENT'):]:
        #     outfile.write(entries)

    blob = []
    with open('html.csv') as f:
            lines = f.readlines()
    for line in lines:
        blob.append(line)
    mega.append(blob)

    # with open('html2.csv', "w") as outfile:
    #     for line in lines:
    #         line = line.replace('\n','')
    #         line = line + ';'
    #         outfile.write(line)
