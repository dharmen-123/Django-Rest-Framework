from django.db import models

# Create your models here.

class Invoice(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(null=True)
    contact=models.IntegerField()
    city=models.CharField(max_length=50)
    price=models.IntegerField()

