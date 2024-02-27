from django.urls import path
from consumer.views import *
urlpatterns = [
    path('home', home, name='home')
]
