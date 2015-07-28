from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product


def product_handler(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    try:
        product = Product.objects.get(pk=product_id)
        return render(request, "product.html", {"product": product})

    except (KeyError, Product.DoesNotExist):
        return render(request, "index.html")