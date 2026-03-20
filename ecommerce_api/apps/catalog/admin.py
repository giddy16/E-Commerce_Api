from django.contrib import admin
from .models import Category, Inventory, ProductTag, Tag, Product, ProductImage

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_id', 'name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'name', 'created_at')
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class InventoryInline(admin.StackedInline):
    model = Inventory
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'Category', 'price', 'is_active', 'sku')
    list_filter = ('Category', 'is_active')
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, InventoryInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'product', 'is_primary', 'created_at')
    list_filter = ('is_primary',)

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'product', 'quantity_in_stock', 'reorder_level', 'updated_at')
    
@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('product_tag_id', 'product', 'tag', 'created_at')