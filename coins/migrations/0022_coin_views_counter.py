# Generated by Django 5.0.7 on 2024-08-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coins", "0021_multioffer"),
    ]

    operations = [
        migrations.AddField(
            model_name="coin",
            name="views_counter",
            field=models.IntegerField(default=0),
        ),
    ]
