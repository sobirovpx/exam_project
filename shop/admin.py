from django.contrib import admin
from django.contrib.auth.models import User, Group

from shop.models import Product, Category


# Register your models here.


# admin.site.register(Product)


# admin.site.unregister(User)
# admin.site.unregister(Group)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'price')


admin.site.register(Product, ProductModelAdmin)
