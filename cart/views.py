from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from myapp.models import Product
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    products = cart.get_products()

    chegirmalar = {}
    for product in products:
        if product.ceil>0:
            chegirmalar[product.id] = product.price - product.price * product.ceil/100

    data = {
        'products': products,
        'chegirmalar':chegirmalar,
    }
    return render(request, 'cart/cart_summary.html', context=data)


def add_cart(request):
    cart = Cart(request)
    print(cart)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product, quantity)


        return JsonResponse({'product_name': product.name})
    return render(request, 'myapp/index.html')
