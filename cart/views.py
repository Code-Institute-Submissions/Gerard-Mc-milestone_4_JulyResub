from django.shortcuts import render


def cart(request):
    """ Returns the cart page """

    return render(request, 'cart/cart.html')
