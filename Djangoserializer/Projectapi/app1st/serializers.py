from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
     id=serializers.IntegerField()
     name=serializers.CharField()
     email=serializers.EmailField()
     rollno=serializers.IntegerField()

     def create(self, validated_data):
        return Student.objects.create(**validated_data)

     def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.rollno = validated_data.get('created', instance.rollno)
        instance.save()
        return instance