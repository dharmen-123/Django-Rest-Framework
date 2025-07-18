from django.shortcuts import render
from .models import Student
from.serializers import StudentSerializer
from django.http import JsonResponse , HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.

def studentapi(req):
    json_data=req.body
    if json_data:
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        x=pythondata['id']
        data = Student.objects.filter(id=x)
        if data :
            showdata=Student.objects.get(id=x)
            serializer=StudentSerializer(showdata)
            return JsonResponse(serializer.data , safe=True)
        else :
            msg={'msg':'Data is not found in database'}
            return JsonResponse(msg) 
    else :
        Alldata=Student.objects.all()
        serializer=StudentSerializer(Alldata,many=True)
        return JsonResponse(serializer.data ,safe=False)
    # return HttpResponse("data not found")