from django.contrib.auth.models import User
from django.db.models import Model, CharField, ForeignKey, DateTimeField, PROTECT
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(Model):
    title = CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = ForeignKey(User, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)