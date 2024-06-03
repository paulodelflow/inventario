from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'pages/delete_product.html', {'product': product})
