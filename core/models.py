from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", max_length=255, blank=True)
    cost = models.IntegerField("Цена")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"

    def __str__(self) -> str:
        return f"{self.name} {self.cost}"
