# Generated by Django 5.0 on 2023-12-18 20:42

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("url", models.URLField(max_length=255, verbose_name="url")),
                (
                    "position",
                    models.PositiveIntegerField(default=1, verbose_name="position"),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="mptt_tree_menu.menuitem",
                    ),
                ),
            ],
            options={
                "verbose_name": "Menu item",
                "verbose_name_plural": "Menu items",
                "ordering": ("name",),
            },
        ),
    ]
