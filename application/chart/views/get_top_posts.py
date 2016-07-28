from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import TopPosts_MH, TopPosts_WH, TopPosts_PVN, TopPosts_RW, TopPosts_BI, TopPosts_ROL, TopPosts_WE

class GetTopPosts(View):
    def get(self, request):
        models_map = {
            "WH": TopPosts_WH,
            "MH": TopPosts_MH,
            "PVN": TopPosts_PVN,
            "RW": TopPosts_RW,
            "BI": TopPosts_BI,
            "ROL": TopPosts_ROL,
            "WE": TopPosts_WE
        }
        response = []
        for brand, TopPosts in models_map.items():
            for model in TopPosts.objects.all():
                response.append(
    				dict(viral_unique = model.viral_unique,
                        unique = model.unique,
                        link = model.link))
        response.sort(key = lambda post: post['viral_unique']/post['unique'])
        response.reverse()
        return JsonResponse(response[:3], safe=False)