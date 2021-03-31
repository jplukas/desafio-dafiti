from django.contrib import admin

from myblog.models import Post, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
