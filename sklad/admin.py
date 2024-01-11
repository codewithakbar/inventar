from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import ProductCategories, Products

@admin.register(ProductCategories)
class ProductCategoriesAdmin(DraggableMPTTAdmin):
    fields = ('name', 'slug')
    list_display = ('tree_actions', 'indented_title', 'name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(DraggableMPTTAdmin):
    fields = ('inventar', 'category', 'user')
    list_display = ('tree_actions', 'indented_title', 'inventar', 'category', 'user')
    search_fields = ['inventar']


