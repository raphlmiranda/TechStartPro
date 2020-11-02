from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from olist.views import CategoryViewSet, ProductViewSet, CsvViewSet

# Set API URL's
router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='Category')
router.register('product', ProductViewSet, basename='Product')
router.register('csv', CsvViewSet, basename='csv')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
