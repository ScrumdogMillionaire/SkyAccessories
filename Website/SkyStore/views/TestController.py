from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", {'name': 'ScrumdogMillionaires'})


def index(request):
    return render(request, "index.html", {})
