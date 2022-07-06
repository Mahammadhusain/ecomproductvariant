from asyncio import proactor_events
from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import cla
from numpy import product
# Create your models here.

class TagModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tag= models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag
class WeightModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    weight= models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.weight)

class ProductNameModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = 'products')

    def __str__(self):
        return self.name
        
    @property
    def products_name(self):
        return ProductModel.objects.filter(product=self.id)


    

class ProductModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductNameModel,on_delete=models.CASCADE) 
    weight = models.ForeignKey(WeightModel,on_delete=models.CASCADE)
    tag = models.ForeignKey(TagModel,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.product.name

    
   
class CartModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.product)+str(self.product.weight)

    @property
    def product_total(self):
        return (self.product.price*self.quantity)