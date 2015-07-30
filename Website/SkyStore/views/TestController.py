
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from SkyStore.forms.customerForm import Register
from SkyStore.forms.addressForm import addressRegister
from SkyStore.forms.addproductForm import AddProductForm
from django.shortcuts import redirect
from SkyStore.forms.loginForm import Login as loginForm
from Website.SkyStore.forms.customerForm import Register
from Website.SkyStore.forms.addressForm import addressRegister
from django.contrib.auth.models import User
from Website.SkyStore.models.Order import Order
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.ProductItem import ProductItem
from Website.SkyStore.models.Address import Address


# from SkyStore.models import Product

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/skystore/')

def home(request):
    products = Product.objects.all()[:6]
    return render(request, "home.html", {'products' : products})

def index(request):
    return render(request, "base.html", {})

def productlist(request):
    return render(request, "productlist.html", {})

def login(request):
    if request.user.is_authenticated():
        return redirect('/skystore/')
    formLogin = loginForm()
    return render(request, "login.html", {})

def basket(request):
    return render(request, "basket.html", {})

def productlist(request):
    return render(request, "productlist.html", {})

def adminpage(request):



    if not request.user.is_staff:
        return redirect('/skystore/')
    products = Product.objects.all()
    orders = Order.objects.all()
    for product in products:
        product.quantity = len(product.productitem_set.filter(status="not_ordered"))
        print 'Product quantity', product.quantity
        if request.method == "POST":
            product_id = str(product.id)
            print request.POST
            if str(product.quantity) != str(request.POST.get(product_id)):
                print product.id, product.quantity, request.POST.get("1")
                ProductItem.objects.create(status='not_ordered', serial_number = '12345', product_id=product.id)
        product.quantity = len(product.productitem_set.filter(status="not_ordered"))
    return render(request, "adminpage.html", {'products': products, 'orders': orders})

def addproduct(request):

    if request.method == "POST":

        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            print 'valid'
            if handle_uploaded_file(request.FILES['fileinput'], request.POST.get('productname')) == 0:
                image_path = 'SkyStore/uploaded/' + request.POST.get('productname') + '.jpg'
                Product.objects.create(name=request.POST.get('productname'), category=request.POST.get('category'), description=request.POST.get('description'), price=request.POST.get('price'), product_image=image_path)
                return redirect("/skystore/adminpage/")
    else:
        form = AddProductForm()
    return redirect("/skystore/adminpage/")

def addproductpage(request):
    return render(request, "addproduct.html", {})

def handle_uploaded_file(f, prod_name):
    with open('SkyStore/uploaded/' + prod_name + '.jpeg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return 0

def addimage(request):
    return render(request, "addproduct.html", {})

def myaccount(request):
    if request.method == "POST":
        print "post"
        # Save Customer
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        dupeUsername = User.objects.filter(username=username)
        if len(dupeUsername) > 0:
            return render(request, "register.html", {'usernameError' : 'User name is taken'})

        dupeEmail = User.objects.filter(email=email)
        if len(dupeEmail) > 0:
            return render(request, "register.html", {'emailError' : 'Email is already used'})

        if confirm_password != password:
            return render(request, "register.html", {'passwordError' : 'Passwords do not match'})

        user = User.objects.create_user(username=username, email=email)
        # Hash the password
        user.set_password(password)
        user.save()
        print "User:", user

        # Save Address
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        postcode = request.POST['postcode']
        county = request.POST['county']
        town = request.POST['town']

        address = Address(street_line1=line1, street_line2=line2, city=town, county=county, postcode=postcode, user=user)
        address.user_id = user.id
        print "address:", user.id
        address.save()

        # Login User

        user = authenticate(username=username, password=password)
        auth_login(request, user)

        return render(request, "accountsettings.html", {})
    return render(request, "accountsettings.html", {})

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
