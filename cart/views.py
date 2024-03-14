from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from myapp.models import Product
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    products = cart.get_products()
    prod_count = cart.get_quantity()

    chegirmalar = {}
    for product in products:
        if product.ceil > 0:
            chegirmalar[product.id] = product.price - product.price * product.ceil / 100

    product_total = {}
    total_ceil = 0
    for product in products:
        if product.ceil>0:
            product_total[product.id] = chegirmalar[product.id]*int(prod_count[str(product.id)])
            total_ceil += product.price * int(prod_count[str(product.id)])
        else:
            product_total[product.id] = product.price * int(prod_count[str(product.id)])
            total_ceil += product.price * int(prod_count[str(product.id)])

    total = 0
    for key, value in product_total.items():
        total += value
    tejov = total_ceil-total

    data = {
        'products': products,
        'chegirmalar':chegirmalar,
        'prod_count':prod_count,
        'product_total':product_total,
        'total':total,
        'total_ceil':total_ceil,
        'tejov':tejov,
    }
    return render(request, 'cart/cart_summary.html', context=data)


def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, quantity)
        count = (cart.get_quantity()[str(product_id)])


        return JsonResponse({'name': product.name, "image": product.image1.url, "quantity":count})
    return render(request, 'myapp/index.html')

def cart_update(request):
    cart = Cart(request)

    if request.GET.get('action') == 'get':
        product_id = request.GET.get('product_id')
        quantity = int(request.GET.get('newVal'))

        cart.update(product_id, quantity)
        return JsonResponse({'price':product_id})

    return render(request, 'cart/cart_summary.html')

def delete_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        cart.delete(request.POST.get('product_id'))
        return JsonResponse({'status':"O'chirildi"})
    return render(request, 'cart/cart_summary.html')
