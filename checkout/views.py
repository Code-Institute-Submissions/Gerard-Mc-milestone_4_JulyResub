from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        order = order_form.save(commit=True)
        order.save()
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse('order'))

    form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'OrderForm': OrderForm,
        'stripe_public_key':'pk_test_51JDyDJHORj0Vb2Rvvj6i5GzPBG5SU3A8Msf6dUF7e1G3wStCT60m82QIUISFL8V9DrkM6VDg3mF48vSLLvABg2AB00WTQtago0',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)

