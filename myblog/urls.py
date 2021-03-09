from django.urls import path, include
from . import views

urlpatterns = [
    path('posts', views.index.as_view(), name='home'),
    path('posts/<int:id>', views.detail.as_view(), name='post_detail'),
    path('users/<int:id>/posts', views.user_posts, name='user_posts')
]