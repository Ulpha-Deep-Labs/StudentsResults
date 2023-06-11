from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import StudentLoginForm

from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'results/dashboard.html', {'section': 'dashboard'})



