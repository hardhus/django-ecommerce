# Generated by Django 4.2.4 on 2024-03-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djangular_pools", "0002_rename_poolitem_pollitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pollitem",
            name="percentage",
        ),
    ]
