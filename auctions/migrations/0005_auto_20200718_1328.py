# Generated by Django 3.0.8 on 2022-12-18 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listings_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='starting_bid',
            new_name='current_price',
        ),
    ]
