from tempfile import template
from django.urls import path
from .views import homepage1,newpage




urlpatterns = [
    path('',homepage1,name='homepage'),
    path('new',newpage,name='newpage')
    
]