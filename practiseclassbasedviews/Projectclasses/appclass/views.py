from django.shortcuts import render, redirect
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu ,many=True)
        return Response(serializer.data)

    def post(req):
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(req, pk):
        stu  = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu )
        return Response(serializer.data)

    def put(req,pk):
        stu  = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(req,pk):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
