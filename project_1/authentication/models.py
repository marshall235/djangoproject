from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)

class vehicle(models.Model):
    name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    customer = models.ForeignKey(customer, on_delete = models.PROTECT,related_name="our_customer")