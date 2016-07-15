import json
import datetime as dt
from urllib import request

access_token = json.load(open("fb_tokens"))

def get_post_ids(brand, next_page=None):  
    if next_page:
        requestUrl = next_page
    else:
        last_24h = dt.datetime.now() - dt.timedelta(hours = 24)
        start = str(int((last_24h-dt.datetime(1970,1,1)).total_seconds()))
        endpoint = "https://graph.facebook.com/v2.5/me/posts?"
        fields = 'id,created_time' 
        requestUrl = endpoint + 'fields='+fields + "&access_token=" + access_token[brand] + '&since=' + start
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    result = json.loads(response.read().decode("utf8"))
    if 'paging' in result:
        result['data'] += get_post_ids(brand, next_page=result['paging']['next'])
    return result['data']

def get_viral_unique(post_id, brand):
    endpoint = 'https://graph.facebook.com/v2.7/'
    fields = '/insights/post_impressions_viral_unique'
    requestUrl = endpoint + post_id + fields + '?access_token=' + access_token[brand]
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = json.loads(response.read().decode("utf8"))    
    return data
