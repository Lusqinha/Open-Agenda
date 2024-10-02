from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=15)
    has_media = models.BooleanField(default=False)
    expiration = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=True, blank=True)
    cost_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    sales_intern = models.ForeignKey(User, on_delete=models.PROTECT)
    

    def __str__(self):
        return str(self.id)