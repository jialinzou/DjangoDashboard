from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from application.chart.models.chart import Top4Posts

class GetTopPosts(View):
    def get(self, request):   
        response = []
        for model in Top4Posts.objects.all():
            response.append(
				dict(rank = model.rank,
					pic = model.pic,
					message = model.message,
					viral_unique = model.viral_unique,
                    link = model.link))
        return JsonResponse(response, safe=False)