from rest_framework import viewsets
from olist.serializer import CategorySerializer, ProductSerializer, CsvSerializer
from olist.models import Category, Product, Csv


# Category API VIEW
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product API VIEW
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CsvViewSet(viewsets.ModelViewSet):

    queryset = Csv.objects.all()
    serializer_class = CsvSerializer