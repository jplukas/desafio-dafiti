from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Post, User
from .forms import PostForm
from django.urls import reverse

class Index(View):
    def get(self, request):
        posts = Post.objects.order_by('-updated_at')
        return render(request, 'index.html', {'posts' : posts})

class Detail(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, 'post.html', {'post' : post})

class UserPosts(View):
    def get(self, request, id):
        posts = Post.objects.filter(author=id).order_by('-updated_at')
        user = User.objects.get(pk=id)
        return render(request, 'index.html', {'posts' : posts, 'user_page' : user})
    
class NewPost(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'edit_post.html', {'form' : form, 'action' : 'new'})

    def post(self, request):
        form = PostForm(request.POST)
        new_post_instance = form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(new_post_instance.id,)))


class EditPost(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form' : form, 'action' : 'edit'})

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        form = PostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(id,)))