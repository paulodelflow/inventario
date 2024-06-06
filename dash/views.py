from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from django import forms
from django.http import JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group mb-0 col-md-6'),
                Column('price', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('stock', css_class='form-group mb-0 col-md-6'),
                Column('description', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group mb-0 col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Agregar Producto', css_class='btn btn-primary')
        )
        # Add custom classes to fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


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
