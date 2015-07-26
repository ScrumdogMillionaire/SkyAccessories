from django.shortcuts import render
from SkyStore.models.Address import Address
# Create your views here.


def home(request):
    return render(request, "home.html", {'name': 'ScrumdogMillionaires'})


def index(request):

    add = Address.objects.get(pk=1)

    return render(request, "index.html", {'add': add})
