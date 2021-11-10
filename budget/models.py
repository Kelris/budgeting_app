from django.db import models


class Expenses(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)


class Income(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
