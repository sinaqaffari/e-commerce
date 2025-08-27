from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.models import Cart
from .models import Order, Order_item
from .forms import OrderCreateForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                Order_item.objects.create(
                    order=order,
                    product=item['producr'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            #cleaning the cart.
            cart.clear()
            return render(request, 'orders/order/created.html', {'order':order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/detail.html', {'order':order})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'admin/orders/order/detail.html', {'order':order})
