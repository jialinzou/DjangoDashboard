from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Runnersworld(View):
    def get(self, request):
        return render(request, "runnersworld.html")