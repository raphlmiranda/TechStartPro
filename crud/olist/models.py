from django.db import models

# Create your models here.

class Category(models.Model):

     name = models.CharField(max_length=35)

     def __str__(self) -> str:
         return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    value = models.FloatField(default=0.0)
    category = models.ManyToManyField(Category, null=True)

    def category_list(self) -> str:
        return ', '.join([p.name for p in self.category.all()])


class Csv(models.Model):    
    
    csvFile = models.FileField(upload_to='files/')
    

    
    