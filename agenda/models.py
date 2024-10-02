from django.contrib.auth.models import User
from products.models import Order
from django.db import models

# Create your models here.
    
class Timetable(models.Model):
    hour = models.TimeField()
    
    def __str__(self):
        return str(self.hour)+'h'

class Scheduling(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    attendant = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.client} -- {self.date} | {self.hour}'
    
    