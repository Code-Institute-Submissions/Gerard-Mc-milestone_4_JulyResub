from django.shortcuts import render


def checkout(request):
    """ Returns the home page """

    return render(request, 'checkout/checkout.html')