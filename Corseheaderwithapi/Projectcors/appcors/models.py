from django.db import models

# Create your models here.

class Alumini(models.Model):
    name=models.CharField(max_length=150)
    empid=models.CharField(max_length=150)
    mobile=models.CharField(max_length=200)
    designation=models.CharField()
    salary=models.CharField()
    city=models.CharField()
    class Meta:
        db_table='Alumini'

    