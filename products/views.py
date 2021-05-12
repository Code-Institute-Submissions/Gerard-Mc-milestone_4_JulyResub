from django.shortcuts import render
from .models import Product, Category
from datetime import datetime


def portfolio(request):
    """ View displays all products and sorts by categories """
    products = Product.objects.all()
    categories = None
    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            products = products.order_by(sort)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            #  The split() splits the string into a list

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/portfolio.html', context)
