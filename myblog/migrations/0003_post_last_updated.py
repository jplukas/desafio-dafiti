# Generated by Django 3.1.7 on 2021-03-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20210308_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]