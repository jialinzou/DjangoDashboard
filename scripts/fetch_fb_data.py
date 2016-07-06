from application.chart.models.chart import VideoViews
from library.fb_report import get_video_views
import datetime

def run():
	response = get_video_views()
	rows = response['data'][0]['values']
	for row in rows:
		time = datetime.datetime.strptime(row['end_time'],'%Y-%m-%dT%H:%M:%S+%f')
		views = row['value']
		VideoViews(id = time, video_views = views).save()