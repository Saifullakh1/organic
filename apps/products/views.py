from django.shortcuts import render
from .models import Product
from apps.blogs.models import Blog


def index(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()[:3]
    return render(request, 'index.html', {'products': products, 'blogs': blogs})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product-detail.html', {'product': product})