# Generated by Django 4.1.7 on 2023-03-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_user"),
        ("shopping_carts", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shoppingcarts",
            name="product",
            field=models.ManyToManyField(
                related_name="shopping_carts", to="products.product"
            ),
        ),
    ]