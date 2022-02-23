from django.urls import path
from .views import *

urlpatterns = [
    path('', auth, name='auth'),
    path('home/', showdata, name='home')
]