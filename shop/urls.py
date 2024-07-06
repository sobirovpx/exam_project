from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import detail

from root import settings
from shop.views import product_list, detail, category_detail, add_comment, search, page_view

urlpatterns = [
                  path('', product_list, name='products'),
                  path('detail/<int:product_id>/', detail, name='detail'),
                  path('category/<int:category_id>/', category_detail, name='category_detail'),
                  path('product/<int:product_id>/add_comment/', add_comment, name='add_comment'),
                  path('search/', search, name='search'),
                  path('page-view/', page_view, name='page_view'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)