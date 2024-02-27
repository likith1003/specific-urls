from django.urls import path
from seller.views import *
urlpatterns = [
    path('home', home, name='home')
]
