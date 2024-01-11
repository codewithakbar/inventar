from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from users.models import User


class ProductCategories(MPTTModel):
    name = models.CharField(max_length=222, verbose_name="Kategoriya Nomi")
    slug = models.SlugField(null=False, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Sklad Kategoriyasi"
        verbose_name_plural = "Sklad Kategoriyalari"

    def __str__(self) -> str:
        return self.name
    

class Products(MPTTModel):
    inventar = models.CharField(max_length=222, verbose_name="Inventar Raqami")

    category = TreeForeignKey(
        ProductCategories,
        on_delete=models.CASCADE, 
        verbose_name="Kategoriya"
    )

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Foydalanuvchi"
    )

    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['inventar']

    class Meta:
        verbose_name = "Sklad Maxsuloti"
        verbose_name_plural = "Sklad Maxsulotlari"

    def __str__(self) -> str:
        return self.inventar + " // " + self.category.name