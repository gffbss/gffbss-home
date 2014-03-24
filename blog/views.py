# Create your views here.
from django.shortcuts import render
from blog.models import Post

# def home(request):
#     return render(request, "home.html")

def index(request):
    # get the blog posts that are puplished
    posts = Post.objects.filter(published=True)
    # return the rendered template
    return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
    # get the Post object
    post = Post.objects.get(slug=slug)
    # return the rendered template
    return render(request, 'blog/post.html', {'post':post})

def landing(request):
    return render(request, "landing.html")