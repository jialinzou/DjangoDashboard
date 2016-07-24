from application.chart.models.chart import TopPosts_MH, TopPosts_WH, TopPosts_PVN, TopPosts_RW, TopPosts_BI, TopPosts_ROL, TopPosts_WE
from library.fb_report import get_post_ids, get_top_viral
import datetime

def run():
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