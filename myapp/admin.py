from django.contrib import admin
from .models import Collection, Category, Product, Season

admin.site.register([Collection, Category, Product, Season])
