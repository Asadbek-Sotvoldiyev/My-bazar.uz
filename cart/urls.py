from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart_summary/', views.cart_summary, name='cart_summary'),
]