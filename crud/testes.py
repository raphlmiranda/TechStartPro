from olist.models import Product, Category

class CategoryTest():

    def __init__(self, name: str):
        self.name = name

    def createCategory(self):
        Category.objects.create(name=self.name)
        print(Category.objects.filter(name=self.name))
    
    def updateCategory(self, name: str):
        Category.objects.filter(name=self.name).update(name=name)
        print(Category.objects.filter(name=name))

    def deleteCategory(self, name: str):
        Category.objects.filter(name=name).delete()
        print(Category.objects.filter(name=name))

class ProductTest():

    def __init__(self, name: str, description: str, value: float, category: str):
        self.name = name
        self.description = description
        self.value = value
        self.category = category

    def createProduct(self):
        Product.objects.create(name=self.name,
                                description=self.description,
                                value=self.value)
        Category.objects.create(name=self.category)
        cat = Category.objects.filter(name=self.category)
        prod = Product.objects.get(name=self.name)
        prod.category.add(*cat)
        print(Product.objects.filter(name=self.name))

    def updateProduct(self, name: str, description: str, value: float):
        Product.objects.filter(name=self.name).update(name=name, description=description, value=value)
        print(Product.objects.filter(name=name, description=description, value=value))
    
    def deleteProduct(self, name: str):
        Product.objects.filter(name=name).delete()
        Category.objects.filter(name=self.category).delete()
        print(Product.objects.filter(name=name))

# Teste Categoria
testCategory = CategoryTest('Testando')
testCategory.createCategory()
testCategory.updateCategory('Testando')
testCategory.deleteCategory('Testando')

#Teste Produto
testProduct = ProductTest(name='Notebook Teste', description='Teste Create', value=900.0, category='Informática')
testProduct.createProduct()
# testProduct.updateProduct(name='Celular Teste', description='Teste Update', value=10.0)
# testProduct.deleteProduct(name='Celular Teste')

