from django.contrib import admin
from .models import Collection, Category, Product, Season, Order, OrderItem

admin.site.register([Collection, Category, Product, Season, Order, OrderItem])
