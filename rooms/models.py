from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from users.models import User
from sklad.models import Products


class RoomsCategory(MPTTModel):
    name = models.CharField(max_length=222, verbose_name="Xona Nomi")
    slug = models.SlugField(null=False, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Xonalar Royxati"
        verbose_name_plural = "Xonalar Royxati"

    def __str__(self) -> str:
        return self.name


class Room(MPTTModel):
    name = models.CharField(max_length=222, verbose_name="Xona nomi")

    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Xona Inventari"
        verbose_name_plural = "Xona Inventari"

    def __str__(self) -> str:
        return self.name


class RoomTableInline(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    category = TreeForeignKey(
        RoomsCategory,
        on_delete=models.CASCADE, 
        verbose_name="Xona Kategoriyasi"
    )

    products = TreeForeignKey(
        Products,
        on_delete=models.CASCADE, 
        verbose_name="Xona Narsalari"
    )

    user = models.ForeignKey(
        User, 
        blank=True, null=True,
        on_delete=models.CASCADE, 
        verbose_name="Biriktirilgan",
    )


