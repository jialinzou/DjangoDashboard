from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import MonthView
from application.chart.models.chart import PageViewsPerHour

# Create your views here.

class GetDataBullet(View):
    def get(self, request):
        response = [
					  {"title":"Revenue","subtitle":"US$, in thousands","ranges":[150,225,300],"measures":[220,270],"markers":[250]},
					  {"title":"today's UV","subtitle":" ","ranges":[20,25,30],"measures":[21,23],"markers":[26]},
		
					]
        return JsonResponse(response, safe=False)