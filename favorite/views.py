from django.http import JsonResponse
from django.shortcuts import render
from favorite.favorite import Favorite
from myapp.models import Product


def favorites(request):
    favorite = Favorite(request)
    products = favorite.get_favorites()
    fav_prod = favorite.favorites()

    data = {
        'products': products,
        'fav_prod': fav_prod,
    }
    return render(request, 'favorite/favorites.html', context=data)

def add_favorite(request):
    favorite = Favorite(request)
    if request.POST.get('action') == 'post':
        favorite.add(request.POST.get('product_id'))
        product = Product.objects.get(id=request.POST.get('product_id'))
        narx = 0
        if product.ceil>0:
            narx = product.price - product.price*product.ceil/100
        else:
            narx = product.price

        return JsonResponse({'name': product.name, 'image':product.image1.url, 'narx':narx})

    return render(request, 'favorite/favorites.html')

def del_favorite(request):
    favorite = Favorite(request)
    if request.POST.get('action') == 'post':
        favorite.dell(request.POST.get('product_id'))

        return JsonResponse({'message':'Deleted'})

    return render(request, 'favorite/favorites.html')
