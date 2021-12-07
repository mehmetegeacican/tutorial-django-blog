from django.shortcuts import render
from .models import Post


#Static Data
posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post #1",
        "content": "The first post content",
        "date": "December 3, 2021"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post #2",
        "content": "The second post content",
        "date": "December 3, 2021"
    },
    
]
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,"./blog/about.html",{'title': "About"})

