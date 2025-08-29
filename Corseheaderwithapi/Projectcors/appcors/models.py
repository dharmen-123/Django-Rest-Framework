from django.db import models

# Create your models here.

class Alumini(models.Model):
    name=models.CharField(max_length=150)
    empid=models.CharField(max_length=150)
    mobile=models.IntegerField()
    designation=models.CharField()
    salary=models.CharField()
    city=models.CharField()
    class Meta:
        db_table='Alumini'

    