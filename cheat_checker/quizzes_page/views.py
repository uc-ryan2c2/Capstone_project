from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def quizzes_view(request, *args, **kwargs):
    return render(request, "quizzes.html", {})

# Create your views here.
