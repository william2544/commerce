# Generated by Django 5.0.1 on 2024-02-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
