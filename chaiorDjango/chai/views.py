from django.shortcuts import render
from .models import ChaiVarites
from django.shortcuts import get_object_or_404
# Create your views here.

def all_chai(request):
    chais = ChaiVarites.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})


def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVarites,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai}) 