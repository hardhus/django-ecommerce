# Generated by Django 4.2.4 on 2024-03-17 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djangular_pools", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PoolItem",
            new_name="PollItem",
        ),
    ]