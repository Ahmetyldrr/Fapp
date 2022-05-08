from tempfile import template
from django.urls import path
from .views import homepage,team



urlpatterns = [
   
    path('',homepage,name='homepage'),
    path('team',team,name='team')
      
]