from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def listdata(req):
    if req.method=='GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    elif req.method=='POST':
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','PATCH','DELETE'])    
def singledata(req, pk):
    id = Student.objects.filter(id=pk)
    if id:
        if req.method=='GET':
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        elif req.method=='PUT':
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        elif req.method=='DELETE':
            stu = Student.object.get(id=pk)
            stu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    else :
        msg={'msg':'id is not found in database'}
        return Response(msg) 