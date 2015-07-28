
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from SkyStore.forms.customerForm import Register
from SkyStore.forms.addressForm import addressRegister
from django.shortcuts import redirect
from SkyStore.forms.loginForm import Login as loginForm
from Website.SkyStore.forms.customerForm import Register
from Website.SkyStore.forms.addressForm import addressRegister
from django.contrib.auth.models import User
# from SkyStore.models import Product

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/skystore/')

def home(request):
    return render(request, "home.html", {})

def index(request):
    return render(request, "base.html", {})

def productlist(request):
    return render(request, "productlist.html", {})

def accountsettings(request):
    return render(request, "accountsettings.html", {})

def login(request):
    formLogin = loginForm()
    return render(request, "login.html", {})

def basket(request):
    return render(request, "basket.html", {})

def productlist(request):
    return render(request, "productlist.html", {})

def myaccount(request):
    if request.method == "POST":
        customerform = Register(request.POST)
        addressform = addressRegister(request.POST)
        print "post"
        if customerform.is_valid() & addressform.is_valid():
            # Save Customer
            print "here"
            username = customerform.cleaned_data['username']
            password = customerform.cleaned_data['password']

            user = customerform.save(commit=False)

            user = User.objects.create_user(username=username, email=user.email)
            # Hash the password
            user.set_password(password)
            user.save()
            print "User:", user

            # Save Address
            address = addressform.save()
            address.user_id = user.id
            print "address:", user.id
            address.save()

            # Login User

            user = authenticate(username=username, password=password)
            auth_login(request, user)

            return render(request, "myaccount.html", {})
    return render(request, "myaccount.html", {})

def register(request):
    addressform = addressRegister()
    customerform = Register()
    return render(request, "register.html", {'customerform': customerform, 'addressform': addressform})

def loginuser(request):
    # Data must be cleaned before passing
    # authenticated_user = authenticate(username=username, password=password)
    # auth_login(request, authenticated_user)
    print "enter login"
    username = request.POST['username']
    password = request.POST['password']

    # username = cleaned_data['username']
    # password = cleaned_data['password']
    user = authenticate(username=username, password=password)

    print user
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/skystore/')
            # Redirect to a success page.
        else:
            return render(request, "login.html", {'error' : 'Account is disabled'})
            # Return a 'disabled account' error message
    else:
        return render(request, "login.html", {'error' : 'Invalid login information'})



# Return all the products in the database
# Can modified by passing search options such as categories
# def products(request):
#     return render(request, "products.html", {'products': Product.object.All()})

# Return a single product in the product page template
# def product(request, product_id=1):
#     return render(request, "product.html", {'product': Product.object.get(id=product_id)})