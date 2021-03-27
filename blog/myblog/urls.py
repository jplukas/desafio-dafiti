from django.urls import path

from myblog.views import (
    Detail,
    EditPost,
    Index,
    IndexTag,
    NewPost,
    NewTag,
    UserPosts,
)

urlpatterns = [
    path('posts', Index.as_view(), name='home'),
    path('posts/new', NewPost.as_view(), name='new_post'),
    path('posts/<int:pk>', Detail.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit', EditPost.as_view(), name='edit_post'),
    path('users/<int:pk>/posts', UserPosts.as_view(), name='user_posts'),
    path('tags/', IndexTag.as_view(), name='tag_index'),
    path('tags/new', NewTag.as_view(), name='new_tag'),
]
