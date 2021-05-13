from django.shortcuts import render


def order(request):
    """ Returns the home page """

    return render(request, 'order/order.html')
