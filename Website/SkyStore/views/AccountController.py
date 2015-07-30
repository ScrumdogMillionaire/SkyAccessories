__author__ = 'bog02'

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.Address import Address
from Website.RewardsApp.models import Reward


def accountsettings(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            address_changed = False
            if request.method == "POST":
                address_changed = update_address(request)

            orders = request.user.order_set.all()
            for order in orders:
                order.products = []
                product_items = order.productitem_set.all()
                for product_item in product_items:
                    print product_item.id
                    product = Product.objects.get(pk=product_item.product_id)
                    if product not in order.products:
                        product.quantity = 1
                        order.products.append(product)
                    else:
                        order.products[order.products.index(product)].quantity += 1

            print "Orders", orders
            delivery_address = get_delivery_address(request.user)
            reward_points = Reward.objects.get(user_id=request.user.id)

            return render(request, "accountsettings.html", {'orders': orders, 'delivery_address': delivery_address,
                                                            'address_updated': address_changed, 'reward_points':reward_points})
        return render(request, "accountsettings.html", {})
    return render(request, "home.html", {})

def get_delivery_address(user):
    return user.address.filter(address_type='default').all()[0]

def update_address(request):
    # Delivery address validator
    street_line1 = request.POST.get('line_1')
    street_line2 = request.POST.get('line_2')
    city = request.POST.get('city')
    county = request.POST.get('county')
    postcode = request.POST.get('postcode')

    stored_address = get_delivery_address(request.user)
    address_changed = False

    if stored_address.street_line1 != street_line1:
        stored_address.street_line1 = street_line1
        stored_address.save(update_fields=['street_line1'])
        address_changed = True

    if stored_address.street_line2 != street_line2:
        stored_address.street_line2 = street_line2
        stored_address.save(update_fields=['street_line2'])
        address_changed = True

    if stored_address.city != city:
        stored_address.city = city
        stored_address.save(update_fields=['city'])
        address_changed = True

    if stored_address.county != county:
        stored_address.county = county
        stored_address.save(update_fields=['county'])
        address_changed = True

    if stored_address.postcode != postcode:
        # Need validation here
        stored_address.postcode = postcode
        stored_address.save(update_fields=['postcode'])
        address_changed = True
    return address_changed

# def create_login(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         password = request.POST['password']
#
#         # check if user already exists
#         if not User.objects.get(username__exact=username):
#             user = User.objects.create_user(username, password)
#             user.save()
#
#
# def create_guest_login(request):
#     pass
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # redirect to account page
#
#             else:
#                 return 'disabled account message'
#
#         else:
#             return 'invalid login message'
#
#
# def change_password():
#     pass
#
#
# def logout(request):
#     logout(request)
#
#
# def home(request):
#     return render(request, "home.html", {'name': 'ScrumdogMillionaires', 'user' : User})
#

