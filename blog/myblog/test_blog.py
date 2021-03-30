# from django.test import TestCase
from django.contrib.auth import get_user_model

import pytest

from myblog.models import Post, Tag
from myblog.templatetags.blog_extratags import intdiv

# Create your tests here.

User = get_user_model()


@pytest.mark.parametrize(
    'value, arg, result',
    [(100, 10, 10), (50, 5, 10), (26, 13, 2), (11, 10, 1), (20, 3, 6)],
)
def test_readtime(value, arg, result):
    assert intdiv(value, arg) == result


@pytest.mark.django_db
def test_tag():
    tag = Tag.objects.create(name='teste')
    user = User.objects.create(username='jao')
    post = Post.objects.create(title='titulo', author=user)
    post.tags.add(tag)
    assert (post.tags.get(name='teste') == tag) and (
        tag.post_set.get(title='titulo') == post
    )
