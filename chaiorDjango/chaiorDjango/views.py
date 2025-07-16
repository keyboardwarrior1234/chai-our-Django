from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello this is my home page")
    return render(request , 'website/index.html')

def about(request):
    #return HttpResponse("Hello this is my About page")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello this is my contant page")
    return render(request, 'website/contact.html')