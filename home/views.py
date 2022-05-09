
from django.shortcuts import render

def homepage1(request):
    return render(request,'home.html')

def newpage(request):
    return render(request,'newpage.html')

