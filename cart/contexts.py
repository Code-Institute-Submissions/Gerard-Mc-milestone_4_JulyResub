from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from portfolio.models import Product, Category

def cart_contents(request):

    cart_items = []
    total = 0
    cart  = request.session.get('cart', {})
    product_count = 0
    order_page_elements_display = False
    for id in cart.items():
        item_price = 0
        category = get_object_or_404(Category, pk=int(id[1]["category"]))
        item_price = category.price
        item_price = item_price * Decimal(id[1]["complexity"])
        if id[1]["fast_delivery"] == "True":
            item_price = item_price * Decimal(settings.FAST_DELIVERY_CHARGE)
        if id[1]["variations"] == 2:
            item_price = round(item_price * Decimal(settings.FAST_DELIVERY_CHARGE), 2)
        item_price = round(item_price, 2)
        total += item_price
        product_count += 1

        if id:
            order_page_elements_display = True

        total += 50
        product_count += 1
        cart_items.append({
            'id': id[0],
            'item_type': id[1]["category"],
            'complexity': id[1]["complexity"],
            'variations': id[1]["variations"],
            'user_description': id[1]["user_description"],
            'fast_delivery': id[1]["fast_delivery"],
            'price': item_price,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'order_page_elements_display': order_page_elements_display,
    }

    return context

 