from application.chart.models.chart import Top4Posts
from library.fb_report import get_post_ids, get_top_viral, get_top4_details
import datetime

def run():
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