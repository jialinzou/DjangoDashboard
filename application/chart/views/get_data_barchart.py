from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import Channel

# Create your views here.

class GetDataBar(View):
    def get(self, request):
        response = []
        for model in Channel.objects.all()[::-1]:
            response.append(dict(State=model.id, may_2015=model.may_2015, april_2015=model.april_2015,
                                     may_2014=model.may_2014))
        return JsonResponse(response, safe=False)