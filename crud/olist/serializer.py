from rest_framework import serializers
from olist.models import Category, Product, Csv

# Serializer Category
class CategorySerializer(serializers.ModelSerializer):
    '''
    Json return {
        'id': int,
        'name': string
    }
    '''

    def to_representation(self, value):
        return value.name

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

    category = CategorySerializer(read_only=False, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'value', 'category']

class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csv
        fields = ['csvFile']