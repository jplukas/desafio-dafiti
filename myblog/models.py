from django.contrib.auth.models import User
from django.db import models
from ckeditor import fields as ckfields
from ckeditor_uploader import fields as ckupload_fields

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = ckfields.RichTextField()
    content = ckupload_fields.RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)