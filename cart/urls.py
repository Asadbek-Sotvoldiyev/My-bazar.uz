from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart_summary/', views.cart_summary, name='cart_summary'),
    path('cart_update/', views.cart_update, name='cart_update'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('order/', views.order, name='order'),
    path('buyurtmalar/', views.buyurtma, name='buyurtmalar'),
]