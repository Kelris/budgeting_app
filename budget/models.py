from datetime import date

from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Expenses(models.Model):
    name = models.CharField(max_length=40, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=''
    )
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.category} {self.value} zł {self.name}"


class Income(models.Model):
    name = models.CharField(max_length=40, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=date.today)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.value} zł {self.name}"
