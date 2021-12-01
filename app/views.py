from django.shortcuts import render

# Create your views here.
from django.views import View


class MyView(View):
    def get(self, request):
        return render(request, 'index.html')

