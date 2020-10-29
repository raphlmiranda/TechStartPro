from rest_framework import viewsets
from olist.serializer import CategorySerializer, ProductSerializer
from olist.models import Category, Product


# Category API VIEW
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product API VIEW
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer