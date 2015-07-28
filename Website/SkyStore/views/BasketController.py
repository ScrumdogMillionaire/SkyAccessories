from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.ShoppingBag import ShoppingBag
from django.core.exceptions import ObjectDoesNotExist


def add_to_basket(request, product_id):
    current_user = request.user
    if current_user.is_authenticated():
        # User is logged in
        try:
            current_user.basket
            print "current user has a basket"
        except ObjectDoesNotExist:
            ShoppingBag.create(user=current_user)
            print "basket created"

        try:
            product = Product.objects.get(id=product_id)
            current_user.basket.product_set.add(product)
            print "product added"
        except ObjectDoesNotExist:
            pass
    else:
        # User is not logged in
        if request.session.get('basket') is None:
            request.session['basket'] = []
        try:
            product = Product.objects.get(id=product_id)
            request.session.get('basket').append(product)
            print "product added"
        except ObjectDoesNotExist:
            pass


def remove_from_basket(request, product_id):
    current_user = request.user
    if current_user.is_authenticated():
        try:
            product = Product.objects.get(id=product_id)
            current_user.basket.product_set.remove(product)
        except ObjectDoesNotExist:
            pass
    else:
        # User is not logged in
        if request.session.get('basket') is None:
            request.session['basket'] = []
        try:
            product = Product.objects.get(id=product_id)
            request.session.get('basket').remove(product)
            print "product removed"
        except ObjectDoesNotExist:
            pass

def basket(request):
    current_user = request.user
    if current_user.is_authenticated():
        try:
            basket = current_user.basket
            print basket

        except AttributeError:

            basket = ShoppingBag.objects.create(user=current_user)
            print basket
            # basket.save()
            print 'basket created'
        basket = basket.get_contents()
    else:
        print request.session.get('basket')
        if request.session.get('basket') is None:
            request.session['basket'] = []
        basket = request.session.get('basket')

    return render(request, 'basket.html', {'basket_contents': basket})