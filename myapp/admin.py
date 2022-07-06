from django.contrib import admin
from .models import TagModel, WeightModel, ProductModel, ProductNameModel, CartModel
# Register your models here.


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ("created_at", "tag", "user","id")[::-1]



@admin.register(WeightModel)
class WeightModelAdmin(admin.ModelAdmin):
    list_display = ("created_at", "weight","user","id")[::-1]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("price", "tag", "weight","product","user","id")[::-1]


@admin.register(ProductNameModel)
class ProductNameModelAdmin(admin.ModelAdmin):
    list_display = ("image", "name","user","id")[::-1]


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("quantity", "product", "user")[::-1]
