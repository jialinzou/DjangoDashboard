from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import UsersPerChannel

class GetUsersPerChannle(View):
    def get(self, request):    
        response = []
        for model in UsersPerChannel.objects.all():
            response.append(
            dict(date = model.date.strftime('%Y%m%d'), 
                users = dict(Other = model.Other,
                            Direct = model.Direct,
                            Email = model.Email,
                            Organic_Search = model.Organic_Search,
                            Paid_Search = model.Paid_Search,
                            Referral = model.Referral,
                            Social = model.Social)))
        return JsonResponse(response, safe=False)