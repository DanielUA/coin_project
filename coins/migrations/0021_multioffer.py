# Generated by Django 5.0.7 on 2024-08-20 07:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coins", "0020_alter_message_options_message_topic"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MultiOffer",
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
                (
                    "status",
                    models.CharField(
                        choices=[("с", "under consideration"), ("d", "done")],
                        default="c",
                        max_length=1,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="multi_offers_made",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "coins_to_get",
                    models.ManyToManyField(related_name="offers_get", to="coins.coin"),
                ),
                (
                    "coins_to_give",
                    models.ManyToManyField(related_name="offers_give", to="coins.coin"),
                ),
                (
                    "responder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="multi_offers_look",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
