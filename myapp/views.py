from django.shortcuts import render, get_object_or_404
from .models import Collection, Category, Product, Season
from django.db.models import Count
from django.views.generic import DetailView, ListView


def index(request):
    seasons = Season.objects.all()
    products = Product.objects.all()
    ceil_products = Product.objects.filter(ceil__gt=1)

    data = {
        'seasons':seasons,
        'products':products,
        'ceil_products':ceil_products,
    }
    return render(request, 'myapp/index.html', context=data)

class ProductDetail(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = "product"


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()

    data = {
        'category':category,
        'products':products,
    }

    return render(request, 'myapp/category.html', context=data)

def season_detail(request, id):
    season = get_object_or_404(Season, id=id)
    products = season.products.all()

    data = {
        'season':season,
        'products':products,
    }

    return render(request, 'myapp/season_products.html', context=data)
