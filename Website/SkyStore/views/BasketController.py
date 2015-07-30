from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import json
from django.core import serializers


def add_to_basket(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print "ID", id
        request = get_basket(request)
        try:
            product = Product.objects.get(id=id)
            product_name = product.name
            product_stock = len(product.productitem_set.filter(status="not_ordered"))
            if product_stock == 0:
                ctx = {
                'number_of_products': len(request.session.get('basket')),
                'product_name': product_name,
                'in_stock': False}
                print "ctx", len(request.session.get('basket'))
                # use mimetype instead of content_type if django < 5
                return HttpResponse(json.dumps(ctx), content_type='application/json')

            current_basket = get_current_basket(request.session.get('basket'))
            if product in current_basket:
                if current_basket[current_basket.index(product)].quantity >= product_stock:
                    print "Product in basket"
                    ctx = {'number_of_products': len(request.session.get('basket')),
                           'product_name': product_name,
                           'in_stock': False}
                    print "ctx", len(request.session.get('basket'))
                    # use mimetype instead of content_type if django < 5
                    return HttpResponse(json.dumps(ctx), content_type='application/json')



            #product = serializers.serialize('json', [product,])
            sessionlist = request.session['basket']
            sessionlist.append(id)
            #sessionlist.append(product)
            print "hi"
            # serialised_list = serializers.serialize('json', sessionlist)
            print "serialised list", sessionlist
            request.session['basket'] = sessionlist
            #
            # request.session['basket'] = sessionlist
            # request.session.get('basket').append(product)
            print "product added"
            ctx = {
                'number_of_products': len(request.session.get('basket')),
                'product_name': product_name,
                'in_stock': True}
            print "ctx", len(request.session.get('basket'))
            # use mimetype instead of content_type if django < 5
            return HttpResponse(json.dumps(ctx), content_type='application/json')
        except ObjectDoesNotExist:
            pass


def remove_from_basket(request, product_id):
    if request.session.get('basket') is None:
        request.session['basket'] = []
    try:
        product = Product.objects.get(id=product_id)
        request.session.get('basket').remove(product)
        print "product removed"
    except ObjectDoesNotExist:
        pass
    return render(request, 'basket.html')


def basket(request):
    request = get_basket(request)
    current_basket = get_current_basket(request.session.get('basket'))
    if len(current_basket) == 0:
        return render(request, 'basket.html', {'no_basket' : True})



    # decoded_json = json.loads(request.session.get('basket'))
    return render(request, 'basket.html', {'current_basket' : current_basket})

def get_basket(request):
    if request.session.get('basket') is None:
        request.session['basket'] = []
    request.session.get('basket')

    return request


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