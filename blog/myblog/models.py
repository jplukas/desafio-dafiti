from django.contrib.auth import get_user_model
from django.db.models import (
    PROTECT,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
)

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Post(Model):
    title = CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = ForeignKey(User, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
