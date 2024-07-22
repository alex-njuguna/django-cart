from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CartItem, Product

def product_list(request):
    """List of all products"""
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})
 
def view_cart(request):
    """Show all items in the cart and tottal price"""
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'myapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    """Add an item to the cart"""
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    messages.info(request, "Item added to cart")
    return redirect('cart:product_list')
 
def remove_from_cart(request, item_id):
    """Remove an item from the cart"""
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    messages.info(request, "Item deleted from cart")
    return redirect('cart:view_cart')
 

