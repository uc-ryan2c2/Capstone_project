from argparse import Namespace
from importlib.resources import path
from unicodedata import name
from django.urls import re_path
from . import views

urlspatterns = [
    path('', views.index, name='index') # this is the main site path (home page)
]