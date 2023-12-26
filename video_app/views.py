from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    featureds = Post.objects.filter(publish = 1).filter(featured = 1)[:4]
    posts = Post.objects.filter(publish = 1).order_by('-date')[:8]
    context = ({'posts': posts, 'featureds': featureds})
    return render(request, 'index.html', context)

def videos(request):
    posts = Post.objects.filter(publish = 1)
    return render(request, 'videos.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__exact = slug)
    return render(request, 'post_detail.html', {'post':post})