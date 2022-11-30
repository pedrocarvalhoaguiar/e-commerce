# Generated by Django 4.1.3 on 2022-11-29 15:22

from django.db import migrations, models
import src.product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=src.product.models.Product.path_to_image_product, verbose_name='image'),
        ),
    ]