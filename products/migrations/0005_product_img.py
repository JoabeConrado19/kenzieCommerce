# Generated by Django 4.1.7 on 2023-03-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img",
            field=models.CharField(default="", max_length=200),
        ),
    ]
