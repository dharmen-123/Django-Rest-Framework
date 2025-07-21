from django.shortcuts import render
from .model import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def listdata(req):
    if req.method=='GET':
        Student = Student.objects.all()
        serializer = StudentSerializer(Student, many=True)
        return Response(serializer.data)
    
    elif req.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)