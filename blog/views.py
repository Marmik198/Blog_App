from django.shortcuts import render
from .models import Post

# Home View
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# About View
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
