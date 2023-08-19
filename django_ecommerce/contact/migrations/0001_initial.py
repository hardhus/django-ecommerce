# Generated by Django 4.2.4 on 2023-08-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactForm",
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
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=250)),
                ("topic", models.CharField(max_length=200)),
                ("message", models.CharField(max_length=1000)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
    ]
