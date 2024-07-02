from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import detail

from root import settings
from shop.views import product_list, detail, category_detail

urlpatterns = [
                  path('', product_list, name='products'),
                  path('detail/<int:product_id>/', detail, name='detail'),
                  path('category/<int:category_id>/', category_detail, name='category_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
