# Generated by Django 4.2.4 on 2024-02-25 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MarketingItem",
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
                ("img", models.CharField(max_length=255)),
                ("heading", models.CharField(max_length=300)),
                ("caption", models.TextField()),
                ("button_link", models.URLField(default="register", null=True)),
                (
                    "button_title",
                    models.CharField(default="View details", max_length=20),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StatusReport",
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
                ("when", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
