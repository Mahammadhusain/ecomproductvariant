from django.contrib import admin
from .models import TagModel, WeightModel, ProductModel, ProductNameModel
# Register your models here.


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ("created_at", "tag", "id")[::-1]



@admin.register(WeightModel)
class WeightModelAdmin(admin.ModelAdmin):
    list_display = ("created_at", "weight","id")[::-1]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("price", "tag", "weight","product","id")[::-1]


@admin.register(ProductNameModel)
class ProductNameModelAdmin(admin.ModelAdmin):
    list_display = ("image", "name","id")[::-1]
