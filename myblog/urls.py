from django.urls import path, include
from . import views

urlpatterns = [
    path('posts', views.index.as_view(), name='home'),
    path('posts/<int:id>', views.detail.as_view(), name='post_detail'),
    path('users/<int:id>/posts', views.user_posts, name='user_posts'),
    path('posts/<int:id>/edit', views.edit_post.as_view(), name='edit_post'),
    path('posts/new', views.new_post.as_view(), name='new_post')
]