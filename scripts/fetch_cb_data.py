from application.chart.models.chart import TopPages
from library.cb_query import get_query
import datetime
import json
import csv

query_ids = json.load(open("cb_query_ids"))

def run():
    domain = 'menshealth.com'
    response = get_query(domain, query_ids[domain])
    rows = csv.DictReader(response.split('\r\n'))
    time = datetime.date.today()-datetime.timedelta(1)
    for row in rows:
        if row['dynamic_title'] == 'Men\'s Health' or row['dynamic_title'] == 'NA':
            continue
        dynamic_title = row['dynamic_title']
        page_avg_time = int(row['page_avg_time'])
        unique_users = int(row['page_uniques'])
        path = domain + row['path']
        TopPages(Date = time, 
                Title = dynamic_title,
                Engaged_time = page_avg_time,
                Unique_users = unique_users,
                Path = path
                ).save()