from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 1, 2019'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 2, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
