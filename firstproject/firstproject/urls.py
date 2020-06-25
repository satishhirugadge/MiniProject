"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from firstapp import views

urlpatterns = [
path('', admin.site.urls),
path('bootcamp1/', views.index1),
path('bootcamp2/', views.index2),
path('bootcamp3/', views.index3),
path('bootcamp4/', views.index4),
path('bootcamp5/', views.index5),
path('index/', views.index6),
path('listing/', views.index7),
path('detail/', views.index8),
path('checkout/', views.index9),
path('register/', views.index10),


]
