from django.shortcuts import render
from django.views.generic import ListView, DetailView
from modules.models import Module

def index(request):
    return render(request, 'modules/modulesList.html')