# Generated by Django 4.1.7 on 2023-03-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300, null=True)),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("category", models.CharField(max_length=100)),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
