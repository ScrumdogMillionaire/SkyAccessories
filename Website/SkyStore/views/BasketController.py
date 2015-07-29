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
                'product_name': product_name}
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


    # decoded_json = json.loads(request.session.get('basket'))
    return render(request, 'basket.html', {'current_basket' : current_basket})

def get_basket(request):
    if request.session.get('basket') is None:
        request.session['basket'] = []
    request.session.get('basket')

    return request