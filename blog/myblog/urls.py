from django.urls import path

from myblog.views import Detail, EditPost, Index, NewPost, UserPosts

urlpatterns = [
    path('posts', Index.as_view(), name='home'),
    path('posts/<int:pk>', Detail.as_view(), name='post_detail'),
    path('users/<int:pk>/posts', UserPosts.as_view(), name='user_posts'),
    path('posts/<int:pk>/edit', EditPost.as_view(), name='edit_post'),
    path('posts/new', NewPost.as_view(), name='new_post'),
]
