from django.shortcuts import render, get_object_or_404
from .models import Collection, Category, Product, Season
from django.db.models import Count
from django.views.generic import DetailView, ListView
from .telegram_message import main
import asyncio
from favorite.favorite import Favorite


def index(request):
    seasons = Season.objects.all()
    products = Product.objects.all()
    ceil_products = Product.objects.filter(ceil__gt=1)
    favorites = Favorite(request)
    fav_prod = favorites.favorites()

    data = {
        'seasons':seasons,
        'products':products,
        'ceil_products':ceil_products,
        'fav_prod':fav_prod,
    }
    return render(request, 'myapp/index.html', context=data)

class ProductDetail(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = "product"


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    favorites = Favorite(request)
    fav_prod = favorites.favorites()

    data = {
        'category':category,
        'products':products,
        'fav_prod':fav_prod,
    }

    return render(request, 'myapp/category.html', context=data)

def season_detail(request, id):
    season = get_object_or_404(Season, id=id)
    products = season.products.all()
    favorites = Favorite(request)
    fav_prod = favorites.favorites()

    data = {
        'season':season,
        'products':products,
        'fav_prod':fav_prod
    }

    return render(request, 'myapp/season_products.html', context=data)

def contact(request):
    if request.POST.get('action')=='post':
        ism = request.POST.get('name')
        email = request.POST.get('email')
        xabar = request.POST.get('message')

        asyncio.run(main(f"Ism: {ism}\nEmail: {email}\nXabar: {xabar}"))
    return render(request, 'myapp/contact.html')

def collection(request, id):
    collection = Collection.objects.get(pk=id)
    products = Product.objects.filter(category__collection=collection)
    print(products)
    favorites = Favorite(request)
    fav_prod = favorites.favorites()

    data = {
        'collection':collection,
        'products':products,
        'fav_prod':fav_prod,
    }
    return render(request, 'myapp/collection.html', context=data)

def about(request):
    return render(request, 'myapp/about.html')