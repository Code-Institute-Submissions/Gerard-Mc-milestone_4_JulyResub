from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse('order'))

    form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'OrderForm': OrderForm,
    }

    return render(request, template, context)

