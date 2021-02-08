from django.shortcuts import render
from .models import Products

# Create your views here.
def view_products(request):
    products = Products.objects.all()
    return render(request, "products.html", {
        "products" : products
    })