from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
# Create your views here.

def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    cart_items = list(cart)
    return render(request, 'cart/cart_detail.html', {'cart':cart, 'cart_items':cart_items})

def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def clean_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')