
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')


def newpage(request):
    return render(request,'newpage.html')

