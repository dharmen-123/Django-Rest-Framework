from rest_framework import serializers
from .models import Alumini

class Aluminiserializer(serializers.ModelSerializer):
    class Meta:
       model=Alumini
       fields='__all__'