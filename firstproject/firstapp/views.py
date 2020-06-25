from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("Hello World")

def index2(request):
    return HttpResponse("My name is Satish Hiru Gadge")

def index3(request):
    return HttpResponse("I am a Writter")

def index4(request):
    return HttpResponse("And my book name is 'You already are in my bad book!!!'")

def index5(request):
    return render(request,"first_app/home.html")

def index6(request):
    return render(request,"first_app/page1.html")

def index7(request):
    return render(request,"first_app/detail.html")

def index8(request):
    return render(request,"first_app/listing.html")

def index9(request):
    return render(request,"first_app/checkout.html")

def index10(request):
    return render(request,"first_app/register.html")
