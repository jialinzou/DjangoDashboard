import urllib
import json

domains = {
		"WH": "womenshealthmag.com",
		"MH": "menshealth.com",
		"PVN": "prevention.com",
		"RW": "runnersworld.com",
		"BI": "bicycling.com",
		"ROL": "rodalesorganiclife.com",
		"WE": "rodalewellness.com"
	}

def get_result():
	result = []
	url = 'http://api.chartbeat.com/live/quickstats/v4?apikey=7f24fb00da5bb5d913b7cab306f71ead&host='
	for site in domains:
		requestUrl = url + domains[site]
		req = urllib.request.Request(requestUrl)
		response = urllib.request.urlopen(req)
		data = json.loads(response.read().decode("utf8"))
		result.append({'peoples': data['data']['stats']['people'], 'site': site})
	return result;