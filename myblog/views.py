from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

class index(View):
    def get(self, request):
        posts = models.Post.objects.order_by('-last_updated')
        return render(request, 'index.html', {'posts' : posts})

class detail(View):
    def get(self, request, id):
        post = models.Post.objects.get(pk=id)
        return render(request, 'post.html', {'post' : post})

def user_posts(request, id):
    posts = models.Post.objects.filter(author=id).order_by('-last_updated')
    user = models.User.objects.get(pk=id)
    return render(request, 'index.html', {'posts' : posts, 'user_page' : user})
    
