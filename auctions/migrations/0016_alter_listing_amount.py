# Generated by Django 5.0.1 on 2024-02-25 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_listing_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='amount',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='auctions.bid'),
        ),
    ]