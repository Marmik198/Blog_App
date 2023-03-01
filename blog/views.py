from django.shortcuts import render

posts = [
    {
      'author': 'Marmik',
      'title': 'Blog 1',
      'content': 'First Post Content',
      'date_posted': 'August 18, 2018'
    },
    {
      'author': 'Keval',
      'title': 'Blog 2',
      'content': 'Second Post Content',
      'date_posted': 'August 12, 2018'
    }
]

# Home View
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# About View
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
