from django.shortcuts import render
from .models import Blog


def detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blogs/blog-detail.html', {'blog': blog})
