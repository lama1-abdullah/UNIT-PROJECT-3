# Generated by Django 5.0 on 2023-12-13 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
    ]
