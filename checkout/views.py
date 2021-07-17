from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from checkout.models import Category
from .models import Order, OrderLineItem
from decimal import Decimal


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        grand_total = 0
        cart = request.session.get('cart', {})
        for item in cart.items():
            item_price = 0
            delivery = False
            complexity = Decimal(item[1]["complexity"])
            variations = Decimal(item[1]["variations"])
            category = get_object_or_404(Category, pk=int(item[1]["category"]))
            item_price = category.price
            item_price = Decimal(item_price) * complexity
            item_price = Decimal(item_price) * variations
            if item[1]["fast_delivery"] == "True":
                    delivery = True
                    item_price = Decimal(item_price) * Decimal(settings.FAST_DELIVERY_CHARGE)
                    item_price = Decimal(round(item_price, 2))
            grand_total+= item_price
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
            'grand_total': grand_total,

        }
        print(grand_total)
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart.items():
                
                item_price = 0
                delivery = False
                complexity = Decimal(item[1]["complexity"])
                variations = Decimal(item[1]["variations"])
                category = get_object_or_404(Category, pk=int(item[1]["category"]))
                item_price = Decimal(category.price)
                item_price = Decimal(item_price) * complexity
                item_price = Decimal(item_price) * variations
                if item[1]["fast_delivery"] == "True":
                    delivery = True
                    item_price = Decimal(item_price) * Decimal(settings.FAST_DELIVERY_CHARGE)
                    item_price = Decimal(round(item_price, 2))

                if id:
                    order_line_item = OrderLineItem(
                        order=order,
                        category=category,
                        complexity=item[1]["complexity"],
                        variations=item[1]["variations"],
                        user_description=item[1]["user_description"],
                        fast_delivery=delivery,
                        lineitem_total=Decimal(item_price),
                        )
                    order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout'))

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect(reverse('order'))

    
        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
                
        form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'OrderForm': OrderForm,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,

        }

    return render(request, template, context)

