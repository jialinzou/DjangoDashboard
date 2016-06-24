from application.chart.models.chart import PageViewsPerHour
from library.ga_report import initialize_analyticsreporting, get_report
import datetime

def run():
	analytics = initialize_analyticsreporting()
	response = get_report(analytics)
	rows = response['reports'][0]['data']['rows']
	for row in rows:
		time = datetime.datetime.strptime(row['dimensions'][0]+row['dimensions'][1],'%Y%m%d%H')
		views = row['metrics'][0]['values'][0]
		PageViewsPerHour(id = time, page_views = views).save()