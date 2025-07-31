from django.contrib import admin
from .models import Product, Contractor, Operation, StorageItem, Document, DocumentItem, Token, Warehouse, Category

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'user']
    list_display_links = ['token', 'user']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'id', 'title', 'modification_count', 'price', 'dt_created', 'dt_updated', 'to_remove']
    list_display_links = ['title', 'price', 'modification_count']
    search_fields = ['title', 'category__name']  # Поиск по наименованию, описанию и категории

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dt_created', 'dt_updated']
    list_display_links = ['title']
    search_fields = ['title']  # Поиск по наименованию контрагента

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['username', 'operation', 'dt_created']
    search_fields = ['username', 'operation']  # Поиск по имени пользователя и операции

@admin.register(StorageItem)
class StorageItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'count', 'dt_created', 'dt_updated', 'to_remove']
    list_display_links = ['product']
    search_fields = ['product__title']  # Поиск по наименованию товара

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination_type', 'apply_flag', 'contractor', 'dt_created', 'dt_updated', 'to_remove']
    list_display_links = ['destination_type', 'contractor']
    search_fields = ['contractor__title', 'destination_type']  # Поиск по наименованию контрагента и типу документа

@admin.register(DocumentItem)
class DocumentItemAdmin(admin.ModelAdmin):
    list_display = ['document', 'product', 'count']
    list_display_links = ['product']
    search_fields = ['document__id', 'product__title']  # Поиск по ID документа и наименованию товара

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location']  # Поиск по имени и местоположению склада

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']  # Поиск по имени категории
