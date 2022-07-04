from django.db import models

# Create your models here.

class TagModel(models.Model):
    tag= models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag
class WeightModel(models.Model):
    weight= models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.weight)

class ProductNameModel(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = 'products')

    def __str__(self):
        return self.name


    @property
    def products_name(self):
        return ProductModel.objects.filter(product=self.id)

class ProductModel(models.Model):
    product = models.ForeignKey(ProductNameModel,on_delete=models.CASCADE) 
    weight = models.ForeignKey(WeightModel,on_delete=models.CASCADE)
    tag = models.ForeignKey(TagModel,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.product.name

    
   
    