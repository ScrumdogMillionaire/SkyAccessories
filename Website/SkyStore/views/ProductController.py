from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product
from Website.SkyStore.models.Address import Address
from django.core.exceptions import ObjectDoesNotExist


def product_handler(request, product_id):
    # p = get_object_or_404(Product, pk=product_id)
    try:
        product = Product.objects.get(pk=product_id)
        product.stock = len(product.productitem_set.filter(status='not_ordered'))
        return render(request, "product.html", {"product": product})

    except (KeyError, Product.DoesNotExist):
        return render(request, "index.html")


def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        print 'Search Term', search_term
        try:
            products = Product.objects.filter(name__icontains=search_term)
            print "Products", products
            return render(request, "search.html", {"products": products})
        except ObjectDoesNotExist:
            return render(request, "search.html", {"noproducts": "No products found."})
    else:
        return render(request, "index.html")

def checkout(request):
    if request.user.is_authenticated():
        # Delivery
        delivery_address = get_delivery_address(request.user)
        print type(delivery_address)


        # Payement

        # Review and Confirm
        return render(request, "checkout.html", {'delivery_address': delivery_address})
    else:
        return render(request, "checkout.html")

def review_order(request):
    current_basket = []
    session_basket = request.session.get('basket')
    for id in session_basket:
        product = Product.objects.get(id=id)

        if product not in current_basket:
            product.quantity = 1
            current_basket.append(product)
        else:
            current_basket[current_basket.index(product)].quantity += 1
            current_basket[current_basket.index(product)].price += product.price


    return render(request, "revieworder.html", {'order': current_basket})

def successful_order(request):



    # product.stock = len(product.productitem_set.filter(status='not_ordered'))

    return render(request, "checkout.html")

def get_delivery_address(user):
    return user.address.filter(address_type='default').all()[0]