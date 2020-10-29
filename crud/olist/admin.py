from django.contrib import admin
from olist.models import Category, Product, Csv
from olist.djangoCsv import djangoCsv
import time


class Categorys(admin.ModelAdmin):
    '''
    Categorys CRUD
    '''
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 5

admin.site.register(Category, Categorys)

class Products(admin.ModelAdmin):
    '''
    Products CRUD
    '''
    list_display = ('name', 'value', 'category_list')
    filter_horizontal = ('category',)
    search_fields = ('name', 'value', 'category__name')
    list_per_page = 5

admin.site.register(Product, Products)

class Csvs(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        '''
        Importing data from CSV to DB
        '''
        obj.is_issued = True
        obj.save()
        djangoCsv().readCsv()

admin.site.register(Csv, Csvs)

