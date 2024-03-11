from django.shortcuts import render
from .cart import Cart

def add_cart():
    cart = Cart(request)
