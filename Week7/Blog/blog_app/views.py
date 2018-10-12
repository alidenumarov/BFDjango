from django.shortcuts import render, redirect

from . models import Post, Comment

# Create your views here.

def blog(request):
    if(request.method == "GET"):
        posts = Post.objects.all()
    return render(request, 'blog.html', {"posts": posts})    