from django.shortcuts import render
from .models import Page, HomeImage, Blog


def home(request):
    data = Page.objects.filter(page_name='home').first()
    images = HomeImage.objects.all()
    return render(request, 'core/home.html', {
        'data': data,
        'images': images
    })


def devops(request):
    data = Page.objects.filter(page_name='devops').first()
    return render(request, 'core/devops.html', {'data': data})


def blogs(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'core/blogs.html', {
        'blogs': blogs
    })
