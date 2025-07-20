from django.shortcuts import render
from .models import ChaiVarites

# Create your views here.

def all_chai(request):
    chais = ChaiVarites.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})