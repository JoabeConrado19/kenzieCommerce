# Generated by Django 4.1.7 on 2023-03-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_remove_product_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=300),
        ),
    ]