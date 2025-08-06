from django.db import models

# Create your models here.

class Invoice(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    city=models.CharField(max_length=100)
    price=models.IntegerField()

    