from django.db import models


class Product(models.Model):
    class CurrencyChoice(models.TextChoices):
        som = "C"
        dollar = "$"
        euro = "€"
    name = models.CharField(
        max_length=250, verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="products", verbose_name="Картинка"
    )
    price = models.IntegerField(
        default=0, verbose_name="Цена"
    )
    currency = models.CharField(
        max_length=100, choices=CurrencyChoice.choices,
        default=CurrencyChoice.dollar, verbose_name="Валюта"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
