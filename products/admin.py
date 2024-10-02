from django.contrib import admin
from products.models import Order, ProductModel
# Register your models here.

admin.site.register(Order)
admin.site.register(ProductModel)