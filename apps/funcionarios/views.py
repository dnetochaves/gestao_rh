from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario

# Create your views here.
def home(request):
    return HttpResponse('Olá')

    
     