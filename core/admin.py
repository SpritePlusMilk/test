from django.contrib import admin
from core import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name", "cost")
    search_fields = ("name", "cost")
