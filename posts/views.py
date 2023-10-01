from django.shortcuts import render, redirect
from posts.models import Product, Category
from datetime import datetime
from posts.forms import CreateProductForm


def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        context_data = {
            'products': product,
            'user':request.user
        }
        return render(request, 'products/product.html', context=context_data)


def category_view(request):
    if request.method == "GET":
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'products/categories.html', context=context_data)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context_data = {
            'product': product
        }
        return render(request, 'products/detail.html', context=context_data)


def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CreateProductForm()
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreateProductForm(data, files)
        if form.is_valid():
            Product.objects.create(
                preview=form.cleaned_data.get('preview'),
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')

        context_data = {
            'form': form
        }
        return render(request, 'products/create.html', context=context_data)
