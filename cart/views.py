import uuid

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from myapp.models import Product, Order, OrderItem
from .cart import Cart
from myapp.telegram_message import main
import asyncio


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
    if request.GET.get('action') == 'get':
        product_id = int(request.GET.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        cart_len = len(cart)
        print(cart_len)
        count = (cart.get_quantity()[str(product_id)])


        return JsonResponse({'name': product.name, "image": product.image1.url, "quantity":count, "cart_len":cart_len})
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

def order(request):

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
        if product.ceil > 0:
            product_total[product.id] = chegirmalar[product.id] * int(prod_count[str(product.id)])
            total_ceil += product.price * int(prod_count[str(product.id)])
        else:
            product_total[product.id] = product.price * int(prod_count[str(product.id)])
            total_ceil += product.price * int(prod_count[str(product.id)])

    total = 0
    for key, value in product_total.items():
        total += value

    try:
        order = Order()
        order.order_id = uuid.uuid4()
        order.total = total
        order.user = request.user
        order.save()
    except:
        raise ValidationError("Order saqlashda xatolik")

    a = 0
    text = f"Buyurtma raqami: {order.order_id}\n\nMahsulotlar:\n"
    try:
        for product in products:
            order_item = OrderItem()
            order_item.order = order
            order_item.product_id = product.id
            order_item.price = product.price
            order_item.name = product.name
            order_item.quantity = prod_count[str(product.id)]
            a += 1
            text += f"{a}.{order_item.name}\nNarxi:{order_item.price}\nSoni:{order_item.quantity}"
            order_item.save()

    except:
        raise ValidationError("OrderItem saqlashda xatolik")


    text+=f"\n\nUmumiy summa: {order.total}\nBuyurtma beruvchi: {request.user.username}\nEmail: {request.user.email}"
    asyncio.run(main(text))
    cart.clear_cart()

    return HttpResponseRedirect(reverse_lazy('cart:buyurtmalar'))

def buyurtma(request):
    cart = Cart(request)
    orders = Order.objects.filter(user=request.user)


    data = {}
    for order in orders:
        data[order] = OrderItem.objects.filter(order_id=order.id)


    return render(request, 'cart/buyurtmalar.html', {"orders": data})