from django.db import models

# Create your models here.

class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()  
    status = models.CharField(max_length=20, default="Created")  
    created_at = models.DateTimeField(auto_now_add=True)
