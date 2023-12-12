# Generated by Django 5.0 on 2023-12-12 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_repair_total'),
        ('products', '0007_alter_product_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repair',
            name='total',
            field=models.IntegerField(),
        ),
    ]