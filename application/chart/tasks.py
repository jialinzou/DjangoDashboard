from celery.task.schedules import crontab
from celery.decorators import periodic_task

from application.chart.models.chart import Top4Posts
from library.fb_report import get_post_ids, get_top_viral, get_top4_details

from application.chart.models.chart import UsersPerChannel
from library.ga_report import initialize_analyticsreporting, get_report

import datetime

@periodic_task(
    run_every=(crontab()),
    name="fetch fackbook data",
    ignore_result=True
)
def fetch_fb_data():
	ids = get_post_ids('MH')
	virals = get_top_viral(ids, 'MH')
	top4 = get_top4_details(virals, 'MH')
	for i, post in enumerate(top4):
		rank = i+1
		pic = post['full_picture']
		message = post['message']
		viral_unique = post['viral_unique']
		link = post['permalink_url']
		Top4Posts(rank = rank, pic = pic, message = message, viral_unique = viral_unique, link = link).save()

@periodic_task(
    run_every=(crontab()),
    name="fetch google data",
    ignore_result=True
)
def fetch_google_data():
	view_id = {
		'apogee': '123191441', #apogee
		'MH': '116151777', #men's health
		'rodale': '124431303' #rodale network
	}
	today = str(datetime.date.today())
	analytics = initialize_analyticsreporting()
	response = get_report(analytics, view_id['rodale'], today)
	rows = response['reports'][0]['data']['rows']
	time = datetime.datetime.strptime(rows[0]['dimensions'][0], '%Y%m%d')
	users = {'(Other)':0, 'Direct':0, 'Email':0, 'Organic Search':0, 
			'Paid Search':0,'Referral':0, 'Social':0}
	for row in rows:
		users[row['dimensions'][1]] = row['metrics'][0]['values'][0]
	UsersPerChannel(date = time, 
					Other = users['(Other)'],
					Direct = users['Direct'],
					Email = users['Email'],
					Organic_Search = users['Organic Search'],
					Paid_Search = users['Paid Search'],
					Referral = users['Referral'],
					Social = users['Social']).save()