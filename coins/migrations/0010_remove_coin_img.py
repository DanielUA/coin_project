# Generated by Django 5.0.7 on 2024-08-03 07:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coins", "0009_alter_coin_material"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coin",
            name="img",
        ),
    ]
