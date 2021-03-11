from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from . import models, forms
from django.urls import reverse

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
    
class new_post(View):
    def get(self, request):
        form = forms.PostForm()
        return render(request, 'edit_post.html', {'form' : form, 'action' : 'new'})

    def post(self, request):
        form = forms.PostForm(request.POST)
        new_post_instance = form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(new_post_instance.id,)))


class edit_post(View):
    def get(self, request, id):
        post = models.Post.objects.get(pk=id)
        form = forms.PostForm(instance=post)
        return render(request, 'edit_post.html', {'form' : form, 'action' : 'edit'})

    def post(self, request, id):
        post = models.Post.objects.get(pk=id)
        form = forms.PostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(id,)))