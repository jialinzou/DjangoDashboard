from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import TopPages

import datetime

class GetTopPages(View):
    def get(self, request):
        yesterday = datetime.date.today()-datetime.timedelta(1)    
        response = []
        for model in TopPages.objects.filter(Date = yesterday).order_by('-Unique_users'):
            response.append(
				dict(Date = model.Date,
					Title = model.Title,
					Unique_users = model.Unique_users,
					Path = model.Path,
					Engaged_time = model.Engaged_time))
        print(response)
        return JsonResponse(response, safe=False)