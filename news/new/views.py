from django.shortcuts import render
from .models import News

# Create your views here.

def home(request):
    n = News.objects.all()
    context = {"n":n}
    return render(request,'new/index.html', context)
