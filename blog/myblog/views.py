from django.conf import settings
from django.db.models.query_utils import select_related_descend
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.db.models import Q

from myblog.forms import PostForm, TagForm
from myblog.models import Post, Tag, User


class Index(View):
    def get(self, request):
        tags = request.GET.getlist('tags')
        posts = Post.objects.order_by('-updated_at')
        if tags:
            posts = posts.filter(tags__in=tags)
            tags = Tag.objects.filter(pk__in=tags).values_list(
                'name', flat=True
            )
        return render(
            request,
            'index.html',
            {
                'posts': posts,
                'words_per_minute': settings.WORDS_PER_MINUTE,
                'tags': tags,
            },
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
        tags = request.GET.getlist('tags')
        posts = Post.objects.filter(author=pk).order_by('-updated_at')
        if tags:
            posts = posts.filter(tags__in=tags)
            tags = Tag.objects.filter(pk__in=tags).values_list(
                'name', flat=True
            )
        user = User.objects.get(pk=pk)
        return render(
            request,
            'index.html',
            {
                'posts': posts,
                'user_page': user,
                'words_per_minute': settings.WORDS_PER_MINUTE,
                'tags': tags,
            },
        )


class IndexTag(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'index_tags.html', {'tags': tags})


class NewTag(View):
    def post(self, request):
        form = TagForm(request.POST)
        form.save()
        return JsonResponse(
            list(Tag.objects.all().values()), safe=False, status=201
        )


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
        forms = {'post': PostForm(instance=post), 'tag': TagForm()}
        return render(
            request,
            'create_update_post.html',
            {'forms': forms, 'action': 'edit', 'header': 'Editar Post'},
        )

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('post_detail', args=(pk,)))

class SearchView(View):
    def get(self, request):
        search_query = request.GET.get('search_query')
        title_contains = Q(title__icontains=search_query)
        summary_contains = Q(summary__icontains=search_query)
        content_contains = Q(content__icontains=search_query)
        posts_content = Post.objects.filter(
            title_contains|
            summary_contains|
            content_contains
        ).order_by('-updated_at')
        posts_tags = Post.objects.filter(tags__name__icontains=search_query)
        return render(request, 'search.html', {
                'posts_content': posts_content,
                'posts_tags': posts_tags,
                'words_per_minute': settings.WORDS_PER_MINUTE,
                'search_query' : search_query,
            })