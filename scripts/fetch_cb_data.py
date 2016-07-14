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
    time = datetime.date.today()
    for row in rows:
        if row['dynamic_title'] == 'Men\'s Health' or row['dynamic_title'] == 'NA':
            continue
        TopPages.objects.update_or_create(
        		Date = time, 
                Title = row['dynamic_title'],
                defaults = {
                	'Engaged_time': int(row['page_avg_time']),
                	'Unique_users': int(row['page_uniques']),
                	'Path' : domain + row['path']
                })