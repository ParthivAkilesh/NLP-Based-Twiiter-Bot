# Generated by Django 4.1.2 on 2022-10-20 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="summarized_text",
            field=models.TextField(default="NS"),
        ),
    ]
