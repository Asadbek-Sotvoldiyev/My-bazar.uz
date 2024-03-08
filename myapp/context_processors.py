from django.db.models import Count

from .models import Collection, Category, Product


def my_context_processor(request):
    collections = Collection.objects.all()
    categories = Category.objects.annotate(product_count=Count('products'))
    products = Product.objects.all()

    ceils = {}
    for product in products:
        if product.ceil:
            ceils[product.pk] = product.price - product.price * product.ceil // 100

    data = {
        'collections': collections,
        'categories':categories,
        'ceils': ceils,
    }

    return data