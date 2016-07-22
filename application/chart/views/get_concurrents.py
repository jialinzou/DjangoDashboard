from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from application.chart.get_url_request import get_result



class GetConcurrents(View):
	def get(self, request):
		result = get_result()
		return JsonResponse(result, safe=False)