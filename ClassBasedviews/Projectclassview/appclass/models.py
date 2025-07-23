from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    city=models.CharField(max_length=60)
    rollno=models.IntegerField()
    class Meta:
        db_table='Student'
        verbose_name="Student"