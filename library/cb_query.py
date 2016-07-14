import json
import datetime as dt
from urllib import request

cb_key = json.load(open("cb_key"))

def cb_live():
    endpoint = "http://api.chartbeat.com/live/toppages/v3/"
    requestUrl = endpoint + "?apikey=" + cb_key + "&host=" + sites["MH"]

    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = json.loads(response.read().decode("utf8"))
    return data

def get_query_id(metrics = 'page_avg_time,page_uniques', dimensions = 'dynamic_title,path'):
    endpoint = 'http://chartbeat.com/query/v2/submit/page/'
    requestUrl = endpoint + '?host=' + sites['MH'] + '&apikey=' + cb_key + '&date_range=day' + \
        '&sort_column=page_uniques&sort_order=desc&limit=12' + \
        '&metrics=' + metrics + '&dimensions=' + dimensions
         
    print(requestUrl)
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    query_id = json.loads(response.read().decode('utf8'))
    return query_id['query_id']
    
def get_query(site, query_id):
    endpoint = "http://chartbeat.com/query/v2/fetch/"
    requestUrl = endpoint + "?apikey=" + cb_key['api-key'] + "&host=" + site + '&query_id=' + query_id

    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = response.read().decode("utf8")
    return data
    