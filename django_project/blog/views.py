from django.shortcuts import render

posts = [
    {
        'author': 'Phathutshedzo',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'February 27, 2020'
    },
    {
        'author': 'Autilia',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'February 28, 2020'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})