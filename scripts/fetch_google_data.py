from application.chart.models.chart import UsersPerChannel, Users_WH, Users_MH, Users_PVN, Users_RW, Users_BI, Users_ROL, Users_WE
from library.ga_report import initialize_analyticsreporting, get_report
import datetime

def run():
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