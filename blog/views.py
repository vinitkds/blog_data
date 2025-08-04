from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Article

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def blog(request):
    posts = Article.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})


def blog_details(request,article_id):
    post = Article.objects.get(id=article_id)
    return render(request, 'blog/blog_details.html',{'post':post})