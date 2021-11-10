from django.contrib import admin

from .models import Expenses, Income

admin.site.register(Income)
admin.site.register(Expenses)
