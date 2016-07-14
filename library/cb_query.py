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
    today = str(dt.date.today())
    endpoint = 'http://chartbeat.com/query/v2/submit/page/'
    requestUrl = endpoint + '?host=' + sites['MH'] + '&apikey=' + cb_key + '&date_range=day' + \
        '&sort_column=page_uniques&sort_order=desc&limit=12&tz=America%2FNew_York' + \
        '&start=' + today + '&end=' + today + '&metrics=' + metrics + '&dimensions=' + dimensions
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    query_id = json.loads(response.read().decode('utf8'))
    return query_id['query_id']
    
def get_query(domain, query_id):
    endpoint = "http://chartbeat.com/query/v2/fetch/"
    requestUrl = endpoint + "?apikey=" + cb_key['api-key'] + "&host=" + domain + '&query_id=' + query_id
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = response.read().decode("utf8")
    return data
    