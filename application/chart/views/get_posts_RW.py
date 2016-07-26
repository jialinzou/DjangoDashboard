from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import TopPosts_RW

class GetRWPosts(View):
    def get(self, request):
        response = []
        for model in TopPosts_RW.objects.all():
            response.append(
                dict(viral_unique = model.viral_unique,
                    link = model.link))
        response.sort(key = lambda post: post['viral_unique'])
        response.reverse()
        return JsonResponse(response[:3], safe=False)