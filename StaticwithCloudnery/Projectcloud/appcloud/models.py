from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField()
    cpassword=models.CharField()
    image=models.ImageField(upload_to='file/')
    
