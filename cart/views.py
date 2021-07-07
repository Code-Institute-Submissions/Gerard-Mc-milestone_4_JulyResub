from django.shortcuts import render
import uuid


def view_cart(request):
    """ Returns the cart page """

    return render(request, 'cart/cart.html')

def add_to_cart(request):
    """ Returns the cart page """
    id = str(uuid.uuid4())
    item_type = request.POST.get('category')
    size = request.POST.get('size')
    user_description = request.POST.get('user_description')
    fast_delivery = request.POST.get('fast_delivery')

    cart_product = {
      "category": item_type, "size": size, "user_description": user_description,
      "fast_delivery": fast_delivery,
}
    product_id = { f"{id}": [cart_product]}
    cart = request.session.get('cart', {})
    cart.__setitem__(id, cart_product)
    request.session['cart'] = cart
    # print(request.session['cart'])

    return render(request, 'order/order.html')