# Generated by Django 5.2.4 on 2025-07-26 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="is_published",
        ),
    ]
