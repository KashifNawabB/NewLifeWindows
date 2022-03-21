"""NewLifeWindows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('page_window', windowPage, name='page_window'),
    path('page_door', doorPage, name='page_door'),
    path('page_contact', contactPage, name='page_contact'),
    path('company_info', companyInfo, name='company_info'),
    path('service_detail', serviceDetail, name='company_info'),
]

# urlpatterns += staticfiles_urlpatterns()
