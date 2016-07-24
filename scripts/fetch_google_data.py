from application.chart.models.chart import UsersPerChannel
from library.ga_report import initialize_analyticsreporting, get_report
import datetime

def run():
	view_id = {
		'apogee': '123191441', #apogee
		'MH': '116151777', #men's health
		'rodale': '124431303' #rodale network
	}
	today = str(datetime.date.today())
	analytics = initialize_analyticsreporting()
	response = get_report(analytics, view_id['rodale'], '2016-07-22')
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