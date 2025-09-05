from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    city=models.CharField(max_length=200)
    contact=models.IntegerField()

    class Meta:
        db_table='Student'