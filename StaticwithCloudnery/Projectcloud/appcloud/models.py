from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage, VideoMediaCloudinaryStorage


# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField()
    cpassword=models.CharField()
    image = models.ImageField(upload_to='image/',storage=MediaCloudinaryStorage() )
    video = models.FileField(upload_to='video/',default='videos/default.mp4',  storage=VideoMediaCloudinaryStorage())
