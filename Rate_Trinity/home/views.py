from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Rate Trinity</h1>\
                            <p>Please give your opinions on your modules and lecturers</p>')