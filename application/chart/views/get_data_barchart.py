from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import VideoViews

# Create your views here.

class GetDataBar(View):
    def get(self, request):
        response = []
        for model in VideoViews.objects.all():
            response.append(dict(date=model.id, VideoViews=model.video_views))
        return JsonResponse(response, safe=False)