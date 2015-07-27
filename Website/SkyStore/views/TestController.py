from django.shortcuts import render

from SkyStore.forms.customerForm import Register
from SkyStore.forms.addressForm import addressRegister
# from SkyStore.models import Product

def home(request):
    return render(request, "home.html", {})

def index(request):
    return render(request, "base.html", {})

def imageslider(request):
    return render(request, "imageslider.html", {})

def productlist(request):
    return render(request, "productlist.html", {})

def accountsettings(request):
    return render(request, "accountsettings.html", {})

def login(request):
    return render(request, "login.html", {})

def myaccount(request):
    if request.method == "POST":
        customerform = Register(request.POST)
        addressform = addressRegister(request.POST)
        if customerform.is_valid() & addressform.is_valid():
            user = customerform.save()
            print 'customer'
            addressform.save(commit=False)
            # addressform.user = user
            # addressform.save()
            print 'address'
            return render(request, "myaccount.html", {})
    return render(request, "myaccount.html", {})

def register(request):
    addressform = addressRegister()
    customerform = Register()
    return render(request, "register.html", {'customerform': customerform, 'addressform': addressform})

# Return all the products in the database
# Can modified by passing search options such as categories
# def products(request):
#     return render(request, "products.html", {'products': Product.object.All()})

# Return a single product in the product page template
# def product(request, product_id=1):
#     return render(request, "product.html", {'product': Product.object.get(id=product_id)})

