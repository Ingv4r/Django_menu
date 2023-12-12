from django.db import models


class Menu(models.Model):
    """Menu db model."""

    name = models.CharField(
        verbose_name="Menu name",
        max_length=30,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Description", max_length=100, db_default="Description"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(
        verbose_name="Menu item name",
        max_length=50,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Description", max_length=100, db_default="Description"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )
    url = models.URLField(
        verbose_name="Url address",
        max_length=50,
        blank=True,
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def __str__(self):
        return self.name
