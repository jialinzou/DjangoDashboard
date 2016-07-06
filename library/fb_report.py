import json
import datetime as dt
from urllib import request

access_token = json.load(open("fb_tokens"))

def get_video_views():
	today = dt.date.today()
	delta = today.isoweekday() % 7 
	last_week = today - dt.timedelta(days = delta)
	last_last_week = last_week - dt.timedelta(days = 8)

	endpoint = "https://graph.facebook.com/v2.5/me/insights/page_video_views_organic?period=week"

	requestUrl = endpoint + "&access_token=" + access_token["MH"] + "&since=" + str(last_last_week) + "&until=" + str(last_week)

	req = request.Request(requestUrl)
	response = request.urlopen(req)
	data = json.loads(response.read().decode("utf8"))
	return data
