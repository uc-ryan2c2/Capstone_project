from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import createUser
from .models import Auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login_page(request, *args, **kwargs):
    return render(request, "login.html", {})
    # Show the login page (username, password)


def account_setup(request, *args, **kwargs):
    # check if the request is post
    form = ""
    if request.method == 'POST':
        form = createUser(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            email = request.POST['email']

            instance = Auth(username=username, email_address=email, password=password)
            instance.save()
        else:
            form = createUser()

        print("data has been saved to DB")
    context = {'form': form}
    return render(request, "accountSetup.html", context)




