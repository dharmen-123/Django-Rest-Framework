from django.shortcuts import render
from .models import Alumini
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .serializers import Aluminiserializer
from rest_framework import generics


# class StudentList(generics.ListCreateAPIView):
#     queryset =Student.objects.all()
#     serializer_class = Studentserializer


# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
from rest_framework import  viewsets
class AluminiViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Alumini.objects.all()
    serializer_class = Aluminiserializer