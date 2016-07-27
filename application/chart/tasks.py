from celery.task.schedules import crontab
from celery.decorators import periodic_task

from application.chart.models.chart import TopPosts_MH, TopPosts_WH, TopPosts_PVN, TopPosts_RW, TopPosts_BI, TopPosts_ROL, TopPosts_WE
from library.fb_report import get_post_ids, get_top_viral

from application.chart.models.chart import UsersPerChannel, Users_WH, Users_MH, Users_PVN, Users_RW, Users_BI, Users_ROL, Users_WE
from library.ga_report import initialize_analyticsreporting, get_report

import datetime

@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="fetch google data",
    ignore_result=True
)
def fetch_google_data():
	view_id = {
		'MH': '116151777', #men's health
		'rodale': '124431303', #rodale network
		'BI': '116179919',
		'WH': '116160397',
		'RW': '112393890',
		'PVN': '100541353',
		'ROL': '112912202',
		'WE': '115482665'
	}
	
	models_map = {
		"WH": Users_WH,
        "MH": Users_MH,
        "PVN": Users_PVN,
        "RW": Users_RW,
        "BI": Users_BI,
        "ROL": Users_ROL,
        "WE": Users_WE,
        "rodale" : UsersPerChannel
	}
	
	today = str(datetime.date.today())
	analytics = initialize_analyticsreporting()
	for brand, Users_model in models_map.items():
		response = get_report(analytics, view_id[brand], '2016-07-26')
		rows = response['reports'][0]['data']['rows']
		time = datetime.datetime.strptime(rows[0]['dimensions'][0], '%Y%m%d')
		users = {'(Other)':0, 'Direct':0, 'Email':0, 'Organic Search':0, 
				'Paid Search':0,'Referral':0, 'Social':0}
		for row in rows:
			users[row['dimensions'][1]] = row['metrics'][0]['values'][0]
		Users_model(date = time, 
						Other = users['(Other)'],
						Direct = users['Direct'],
						Email = users['Email'],
						Organic_Search = users['Organic Search'],
						Paid_Search = users['Paid Search'],
						Referral = users['Referral'],
						Social = users['Social']).save()

@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="fetch fackbook data",
    ignore_result=True
)
def fetch_fb_data():
	models_map = {
		"WH": TopPosts_WH,
        "MH": TopPosts_MH,
        "PVN": TopPosts_PVN,
        "RW": TopPosts_RW,
        "BI": TopPosts_BI,
        "ROL": TopPosts_ROL,
        "WE": TopPosts_WE
	}
	for brand, TopPosts in models_map.items():
		ids = get_post_ids(brand)
		top3 = get_top_viral(ids, brand)
		for i, post in enumerate(top3):
			rank = i+1
			viral_unique = post['viral_unique']
			link = post['permalink_url']
			TopPosts(rank = rank, viral_unique = viral_unique, link = link).save()
