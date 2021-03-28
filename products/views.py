from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    """ View to display the products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/portfolio.html', context)