from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This is form the home page
def index(request):
    return HttpResponse('<h1>Hey, Welcome</h1>')
