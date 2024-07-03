from django.contrib import admin
from django.contrib.auth.models import User, Group

from shop.models import Product, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# @admin.register(Comment)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ('email', 'body')
#

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'price')


admin.site.register(Product, ProductModelAdmin,)
