from django.contrib import admin

from .models import Category, Expenses, Income

admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Expenses)
