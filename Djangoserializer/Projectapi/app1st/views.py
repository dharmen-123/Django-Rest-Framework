from django.shortcuts import render
from .models import Student
from.serializers import StudentSerializers
from django.http import JsonResponse , HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io


def alldata(req):
    data=Student.objects.all()
    serializer=StudentSerializers(data,many=True)
    print(data)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

def singledata(req):
    data=Student.objects.get(id=2)
    serializer=StudentSerializers(data)
    print(data)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def studentapi(req):
    if req.method =='POST':
        jsondata=req.body
        stream=io.BytesIO(jsondata)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data is succusfully accept and save"}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
            # return JsonResponse(res)
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')

@csrf_exempt
def mypatch(req,pk):
    if req.method=='PATCH':
        jsondata=req.body
        stream=io.BytesIO(jsondata)
        pynewdata=JSONParser().parse(stream)
        pyolddata=Student.objects.get(id=pk)
        serializer=StudentSerializers(pyolddata,data=pynewdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data is successfully updated"}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
            # return JsonResponse(res)
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    elif req.method=='PUT':
        jsondata=req.body
        stream=io.BytesIO(jsondata)
        pynewdata=JSONParser().parse(stream)
        pyolddata=Student.objects.get(id=pk)
        serializer=StudentSerializers(pyolddata,data=pynewdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data is successfully updated"}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
            # return JsonResponse(res)
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    elif req.method=='DELETE':
        pyolddata=Student.objects.get(id=pk)
        serializer=StudentSerializers(data=pyolddata,partial=True)
        if serializer.is_valid():
            serializer.delete()
            res={'msg':"Data is successfully updated"}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
            # return JsonResponse(res)
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
        pass

       

