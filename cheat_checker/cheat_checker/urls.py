"""cheat_checker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# import custom pages
from classes_page.views import classes_view
from authentication.views import login_page, account_setup
from quizzes_page.views import quizzes_view

urlpatterns = [
    # classes page
    path('classes', classes_view, name='home'),

    # login/account setup page
    path('', login_page, name='login'),
    path('accountSetup/', account_setup, name='accountSetup'),

    # quizzes page
    path('quizzes/', quizzes_view, name='quizzes'),

    # admin page (database)
    path('admin/', admin.site.urls),
]
