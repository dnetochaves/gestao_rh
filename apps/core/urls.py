from django.urls import include
from .views import profile
from .views import index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('profile', profile, name='profile'),
]
