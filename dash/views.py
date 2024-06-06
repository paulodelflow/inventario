from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from django import forms
from django.http import JsonResponse


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image']

def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products})

def delete_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('index')
    return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products, 'form': form})

