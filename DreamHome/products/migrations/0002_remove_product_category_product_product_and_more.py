# Generated by Django 5.0 on 2023-12-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='choose_co',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Beige', 'Beige'), ('Brown', 'Brown'), ('Green', 'Green'), ('Blue', 'Blue')], default='Cultural', max_length=70),
        ),
    ]
