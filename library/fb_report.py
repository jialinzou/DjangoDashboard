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
        fields = 'id,type,permalink_url' 
        requestUrl = endpoint + 'fields='+fields + "&access_token=" + access_token[brand] + '&since=' + start
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    result = json.loads(response.read().decode("utf8"))
    if 'paging' in result:
        result['data'] += get_post_ids(brand, next_page=result['paging']['next'])
    return list(filter(lambda x: x['type'] == 'link', result['data']))

def get_viral_unique(post_id, brand):
    endpoint = 'https://graph.facebook.com/v2.7/'
    fields = '/insights/post_impressions_viral_unique'
    requestUrl = endpoint + post_id + fields + '?access_token=' + access_token[brand]
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = json.loads(response.read().decode("utf8"))    
    return data['data'][0]['values'][0]['value']

def get_top_viral(post_ids, brand):
    viral_list = []
    for post in post_ids:
        viral = get_viral_unique(post['id'], brand)
        viral_list.append({'id':post['id'], 'viral_unique':viral, 'permalink_url':post['permalink_url']})
    viral_list.sort(key = lambda viral:viral['viral_unique'])
    viral_list.reverse()
    return viral_list[:3]

def get_post_details(post_id, brand):
    endpoint = 'https://graph.facebook.com/v2.7/'
    fields = '?fields=full_picture,permalink_url,message'
    requestUrl = endpoint + post_id + fields + '&access_token=' + access_token[brand]
    req = request.Request(requestUrl)
    response = request.urlopen(req)
    data = json.loads(response.read().decode("utf8")) 
    return data

def get_top4_details(viral_list, brand):
    top4 = []
    for viral in viral_list[:4]:
        details = get_post_details(viral['id'],'MH')
        details['viral_unique'] = viral['viral_unique']
        top4.append(details)
    return top4
