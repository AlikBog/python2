from django.shortcuts import render
from .models import *
from django.views.generic import *

# Create your views here.

def home(request):
    n = News.objects.all()
    context = {"context":n}
    return render(request,'new/index.html', context)


