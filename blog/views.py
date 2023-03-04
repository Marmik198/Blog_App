from django.shortcuts import render
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView
)
from pprint import pprint
from .models import Post

# Home View
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

# About View
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Post Details View
class PostDetailView(DetailView):
    model = Post

# Post Create View
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)