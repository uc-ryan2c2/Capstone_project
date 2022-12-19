from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login_page(request, *args, **kwargs):
    return render(request, "login.html", {})
    # Show the login page (username, password)


def account_setup(request, *args, **kwargs):
    return render(request, "accountSetup.html", {})

    # This is where the user will create an account
    # Link their account to canvas with the generated API key
    # Show how to generate the API key
    # save all the information to the database
