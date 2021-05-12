from django.shortcuts import render
from .models import Product, Category


def portfolio(request):
    """ View displays all products and sorts by categories """
    # All products loaded when page loads.
    products = Product.objects.all()
    # categories_string is a conversion from list to string
    # to be used in a query string for user sorting options in portfolio.html.
    categories_string = ""
    categories = Category.objects.values('name')

    if request.GET:
        if 'category' in request.GET:
            # split() splits the string into a list
            categories = request.GET['category'].split(",")
            #  Filter products to the above category/categories.
            products = products.filter(category__name__in=categories)
            # Converting the list back to string
            if len(categories) > 1:
                for i in range(len(categories)):
                    # Adds comma to maintain the established format.
                    categories_string += "" + categories[i] + ","
                # Removes comma after final word.
                categories_string = categories_string[:-1]
                print(categories_string)
            else:
                # Converts lists with a single item to string.
                for i in categories:
                    categories_string += i
            # Takes sort parameter value from URL.
            if 'sort' in request.GET:
                sort = request.GET['sort']
                sortkey = sort
                # Checks the direction param value.
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    # Inverts the sort direction.
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                        products = products.order_by(sortkey)
                # Sort products by chosen entity field.
                products = products.order_by(sortkey)

    context = {
        'products': products,
        'category': categories_string,
    }

    return render(request, 'products/portfolio.html', context)
