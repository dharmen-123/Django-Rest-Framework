from django.shortcuts import render, redirect
from .models import Student
from .serializers import StudentSerializer
# Create your views here.



 ###### <----------------------- API USING VIEWS ----------------->
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class StudentList(APIView):
#     def get(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(id=pk)
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         stu = self.get_object(pk)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         stu = self.get_object(pk)
#         serializer = StudentSerializer(stu, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         stu = self.get_object(pk)
#         stu.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

###### <------------ USING MIXIN BASED VIEWS -------------------->


# from rest_framework import mixins
# from rest_framework import generics
# class StudentList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

##### <----------------- GENERIC BASED VIEWS ------------------>

from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer