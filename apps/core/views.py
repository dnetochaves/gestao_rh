from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@login_required
def profile(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/profile.html', data)

