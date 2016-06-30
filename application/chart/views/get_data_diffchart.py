from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import MonthByMonth 

class GetDataDiff(View):
    def get(self, request):
        response = []
        for model in MonthByMonth.objects.all():
            response.append(dict(date=model.id.strftime("%Y%m%d"), Actual=model.actual, Forecast=model.forest))
        return JsonResponse(response, safe=False)