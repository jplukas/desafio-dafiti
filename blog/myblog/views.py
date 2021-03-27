from django.conf import settings
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from myblog.forms import PostForm, TagForm
from myblog.models import Post, Tag, User


class Index(View):
    def get(self, request):
        posts = Post.objects.order_by('-updated_at')
        return render(
            request,
            'index.html',
            {'posts': posts, 'words_per_minute': settings.WORDS_PER_MINUTE},
        )


class Detail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(
            request,
            'post.html',
            {'post': post, 'words_per_minute': settings.WORDS_PER_MINUTE},
        )


class UserPosts(View):
    def get(self, request, pk):
        posts = Post.objects.filter(author=pk).order_by('-updated_at')
        user = User.objects.get(pk=pk)
        return render(
            request,
            'index.html',
            {
                'posts': posts,
                'user_page': user,
                'words_per_minute': settings.WORDS_PER_MINUTE,
            },
        )


class IndexTag(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'index_tags.html', {'tags': tags})


class DetailTag(View):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        posts = Post.objects.filter(tags__id=pk).order_by('-updated_at')
        return render(
            request,
            'index.html',
            {
                'posts': posts,
                'tag': tag,
                'words_per_minute': settings.WORDS_PER_MINUTE,
            },
        )


class NewTag(View):
    def post(self, request):
        form = TagForm(request.POST)
        form.save()
        return JsonResponse(list(Tag.objects.all().values()), safe=False)


class NewPost(View):
    def get(self, request):
        forms = {'post': PostForm(), 'tag': TagForm()}
        return render(
            request,
            'create_update_post.html',
            {'forms': forms, 'action': 'new', 'header': 'Novo Post'},
        )

    def post(self, request):
        form = PostForm(request.POST)
        new_post_instance = form.save()
        return HttpResponseRedirect(
            reverse('post_detail', args=(new_post_instance.id,))
        )


class EditPost(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(
            request,
            'create_update_post.html',
            {'form': form, 'action': 'edit', 'header': 'Novo Post'},
        )

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(pk,)))
