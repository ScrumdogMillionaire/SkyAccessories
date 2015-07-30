from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.Address import Address
from Website.SkyStore.models.Order import Order
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import date, timedelta
from django.db import OperationalError
import requests
from Website.RewardsApp.models import Reward


def product_handler(request, product_id):
    # p = get_object_or_404(Product, pk=product_id)
    try:
        product = Product.objects.get(pk=product_id)
        try:
            product.stock = len(product.productitem_set.filter(status='not_ordered'))
        except OperationalError:
            # Handle no stock
            product.stock = 0
        return render(request, "product.html", {"product": product})

    except (KeyError, Product.DoesNotExist):
        return render(request, "index.html")


def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        print 'Search Term', search_term
        try:
            products = Product.objects.filter(Q(name__icontains=search_term) | Q(category__iexact=search_term))
            print "Products", products
            return render(request, "search.html", {"products": products})
        except ObjectDoesNotExist:
            return render(request, "search.html", {"noproducts": "No products found."})
    else:
        return render(request, "index.html")

def checkout(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return render(request, "checkout.html")
        else:
            current_basket = get_current_basket(request.session.get('basket'))
            for product in current_basket:
                if product.quantity > len(product.productitem_set.filter(status='not_ordered')):
                    # Not enough stock
                    return (request, "basket.html", {'current_basket' : current_basket})

            # Delivery
            delivery_address = get_delivery_address(request.user)
            print type(delivery_address)


            # Payement

            # Review and Confirm
            return render(request, "checkout.html", {'delivery_address': delivery_address})
    else:

        return render(request, "checkout.html")

def review_order(request):
    if request.method == "POST":
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
        print "stored address", stored_address


        current_basket = get_current_basket(request.session.get('basket'))
        price = float(get_basket_price(current_basket))*100
        return render(request, "revieworder.html", {'order': current_basket, 'address_updated' : address_changed, 'price': price})
    return render(request, "home.html")

def successful_order(request):
    if request.method == "POST":
        token = request.POST.get('stripeToken')
        print 'token', token
        current_basket = get_current_basket(request.session.get('basket'))
        order = Order.objects.create(creation_date=date.today(),
                                     expected_delivery_date=timedelta(days=3)+date.today(),
                                     status= 'Order Placed',
                                     user=request.user,
                                     price=get_basket_price(current_basket))
        print "order", order
        for product in current_basket:
            product_items = product.productitem_set.filter(status='not_ordered')[:product.quantity]
            for i in product_items:
                # Update the stock
                i.status = 'ordered'
                i.order = order
                i.save()
                print "i", i
        request.session['basket'] = []
        rewards = Reward.objects.get(user_id = request.user)
        rewards.points += order.price*10
        rewards.save()

        send_simple_message(request.user, order)

        return render(request, "successfulorder.html", {'order': order})
    return render(request, "home.html")






    # product.stock = len(product.productitem_set.filter(status='not_ordered'))



def get_delivery_address(user):
    return user.address.filter(address_type='default').all()[0]

def get_current_basket(session_basket):
    current_basket = []
    for id in session_basket:
        product = Product.objects.get(id=id)

        if product not in current_basket:
            product.quantity = 1
            current_basket.append(product)
        else:
            current_basket[current_basket.index(product)].quantity += 1
            current_basket[current_basket.index(product)].price += product.price
    return current_basket

def get_basket_price(basket):
    price = 0
    for i in basket:
        price += (i.price * i.quantity)
    return price

def send_simple_message(customer, order):
    order_string = "Hi "+ customer.username+ ",\nYour order has been successfully placed.\nDate Order Placed: "+ str(order.creation_date) +"\nDelivery Date: "+ str(order.expected_delivery_date) +"\n"
    product_items = order.productitem_set.all()
    order.products = []
    for product_item in product_items:
        print product_item.id
        product = Product.objects.get(pk=product_item.product_id)

        if product not in order.products:
            product.quantity = 1
            order.products.append(product)
        else:
            order.products[order.products.index(product)].quantity += 1
    for i in order.products:
        order_string += "Name: "+ i.name + " : "+ unichr(163) + str(i.price) + "\n"
    order_string += "______________________\n"
    order_string += "Total cost: "+ unichr(163) + str(order.price)+"\n"
    order_string += "______________________\n\n"
    order_string += "Delivery Address:\n"
    address = get_delivery_address(customer)
    order_string += address.street_line1 +"\n"
    order_string += address.street_line2 +"\n"
    order_string += address.city +"\n"
    order_string += address.county +"\n"
    order_string += address.postcode +"\n\n"
    order_string+= "Thanks for your order."

    return requests.post(
       "https://api.mailgun.net/v3/sandbox2247e4430337465194da28f52b4e090b.mailgun.org/messages",
       auth=("api", "key-49ea010ba13f50e4b7c9bc12e258132b"),
       data={"from": "Mailgun Sandbox <postmaster@sandbox2247e4430337465194da28f52b4e090b.mailgun.org>",
             "to": customer.username+ " <"+customer.email+">",
             "subject": "Your order has been confirmed",
             "text": order_string})