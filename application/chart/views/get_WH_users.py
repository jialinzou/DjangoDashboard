from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import Users_WH

class GetWHUsers(View):
    def get(self, request):    
        response = []
        for model in Users_WH.objects.order_by('-date')[:8][::-1]:
            response.append(
            dict(date = model.date.strftime('%Y%m%d'), 
                users = dict(#Other = model.Other,
                            Direct = model.Direct,
                            Email = model.Email,
                            Search = model.Organic_Search,
                            #Paid_Search = model.Paid_Search,
                            Referral = model.Referral,
                            Social = model.Social)))
        return JsonResponse(response, safe=False)