from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from portfolio.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    cart  = request.session.get('cart', {})
    product_count = 0
    for id in cart.items():
        total += 50
        product_count += 1
        cart_items.append({
            'id': id[0],
            'item_type': id[1]["category"],
            'complexity': id[1]["complexity"],
            'variations': id[1]["variations"],
            'user_description': id[1]["user_description"],
            'fast_delivery': id[1]["fast_delivery"],
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context

 