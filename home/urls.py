from tempfile import template
from django.urls import path
from .views import homepage,newpage



urlpatterns = [
   
    path('home',homepage,name='homepage'),
    path('new',newpage,name='newpage')
    
]