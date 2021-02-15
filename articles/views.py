from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post

def HomeView(request):
    posts = Post.objects.all()
    template = loader.get_template('articles/home.html')
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context, request))

def post_detail(request, slug):
    #return HttpResponse(slug)
    article=Post.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':article})