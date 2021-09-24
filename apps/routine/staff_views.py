from django.shortcuts import render
from .models import *


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def add_assignment(request):
    return render(request, 'staff/add_assignment.html')