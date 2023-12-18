from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField('url', max_length=255)
    position = models.PositiveIntegerField('position', default=1)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ('position',)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Menu item'
        verbose_name_plural = "Menu items"
