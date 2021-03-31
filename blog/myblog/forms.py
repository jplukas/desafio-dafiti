from django.forms import ModelForm

from myblog.models import Post, Tag


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'summary', 'content', 'tags']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
