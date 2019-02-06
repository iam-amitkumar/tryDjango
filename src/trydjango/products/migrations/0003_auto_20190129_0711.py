# Generated by Django 2.0.7 on 2019-01-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default='example@sample.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]