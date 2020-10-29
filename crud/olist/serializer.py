from rest_framework import serializers
from olist.models import Category, Product

# Serializer Category
class CategorySerializer(serializers.ModelSerializer):
    '''
    Json return {
        'id': int,
        'name': string
    }
    '''
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer Product
class ProductSerializer(serializers.ModelSerializer):
    '''
    Json return {
        'id': int,
        'name': string,
        'value': float,
        'category': int
    }
    '''

    class Meta:
        model = Product
        fields = ['id', 'name', 'value', 'category']