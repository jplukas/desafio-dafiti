from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import PostForm
from .models import Post, User


class Index(View):
    def get(self, request):
        posts = Post.objects.order_by('-updated_at')
        return render(
            request,
            'index.html',
            {'posts': posts, 'wpm': settings.WORDS_PER_MINUTE},
        )


class Detail(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(
            request,
            'post.html',
            {'post': post, 'wpm': settings.WORDS_PER_MINUTE},
        )


class UserPosts(View):
    def get(self, request, id):
        posts = Post.objects.filter(author=id).order_by('-updated_at')
        user = User.objects.get(pk=id)
        return render(
            request,
            'index.html',
            {
                'posts': posts,
                'user_page': user,
                'wpm': settings.WORDS_PER_MINUTE,
            },
        )


class NewPost(View):
    def get(self, request):
        form = PostForm()
        return render(
            request,
            'create_update_post.html',
            {'form': form, 'action': 'new', 'header': 'Novo Post'},
        )

    def post(self, request):
        form = PostForm(request.POST)
        new_post_instance = form.save()
        return HttpResponseRedirect(
            reverse('post_detail', args=(new_post_instance.id,))
        )


class EditPost(View):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        form = PostForm(instance=post)
        return render(
            request,
            'create_update_post.html',
            {'form': form, 'action': 'edit', 'header': 'Novo Post'},
        )

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        form = PostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(id,)))
