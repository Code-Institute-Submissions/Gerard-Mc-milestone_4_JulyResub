from django.contrib import admin
from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'name',
        'friendly_name',
    )

    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)