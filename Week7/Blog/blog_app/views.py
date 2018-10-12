from django.shortcuts import render, redirect
from . forms import PostForm, CommentForm
from . models import Post, Comment

# Create your views here.

def blog(request):
    if(request.method == "GET"):
        posts = Post.objects.all()
    return render(request, 'blog.html', {"posts": posts})

def add_block(request):
    if (request.method == 'POST'):
        if request.user.is_authenticated:
            author = request.user.username
        else:
            author = "anonymous author"
        title = request.POST['title']
        text =  request.POST['text']
        post = Post(author = author, title = title, text = text)
        post.save()
        return redirect('/blog')
    return render(request, 'add_blog.html')