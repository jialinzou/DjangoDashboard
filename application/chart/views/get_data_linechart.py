from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import MonthView
from application.chart.models.chart import PageViewsPerHour

# Create your views here.

class GetDataLine(View):
    def _get(self, request):
        response = []
        for model in MonthView.objects.all():
            response.append(dict(date=self.month_to_number(model.id), Desktop=model.desktop, Mobile=model.mobile,
                                     total_2015=model.total_2015, total_2014=model.total_2014))
        return JsonResponse(response, safe=False)
        
    def month_to_number(self, mon):
        return {
            'January': '20110101',
            'Febuary': '20110201',
            'March': '20110301',
            'April': '20110401',
            'May': '20110501',
            'June': '20110601',
            'July': '20110701',
            'August': '20110801',
            'September': '20110901',
            'October': '20111001',
            'November': '20111101',
            'December': '20111201'
        }[mon]

    def get(self, request):
        response = []
        for model in PageViewsPerHour.objects.all():
            response.append(dict(date = model.id.strftime('%Y%m%d%H'), page_views = model.page_views))
        return JsonResponse(response, safe=False)

