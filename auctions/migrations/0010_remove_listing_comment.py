# Generated by Django 5.0.1 on 2024-02-21 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_comment_content_comment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comment',
        ),
    ]
