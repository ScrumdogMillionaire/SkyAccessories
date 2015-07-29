from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import resolve
from Website.SkyStore.models.Product import Product
from django.core.exceptions import ObjectDoesNotExist


def product_handler(request, product_id):
   #p = get_object_or_404(Product, pk=product_id)
   try:
       product = Product.objects.get(pk=product_id)
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
