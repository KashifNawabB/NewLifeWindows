from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home2.html')

def windowPage(request):
    return render(request, 'page-window.html')

def doorPage(request):
    return render(request, 'page-door.html')

def contactPage(request):
    return render(request, 'page-contact.html')

def companyInfo(request):
    return render(request, 'about-company-infomation.html')