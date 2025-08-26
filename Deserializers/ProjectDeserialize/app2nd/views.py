from django.shortcuts import render
from .models import Student
from.serializers import StudentSerializer
from django.http import JsonResponse , HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io


######## All Methods in function 
@csrf_exempt
def studentapi(req):
    if req.method=="GET":
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
    elif req.method=="POST":
        jsondata=req.body
        stream=io.BytesIO(jsondata)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is successfully saved in database'}
            return JsonResponse(res)
        jdata= JSONRenderer().render(serializer.errors)
        return HttpResponse(jdata, content_type='application/json')
    
    elif req.method=="PUT":
        jsondata=req.body
        stream=io.BytesIO(jsondata)
        pynewdata=JSONParser().parse(stream)
        pk=pynewdata['id']
        pyolddata=Student.objects.get(id=pk)
        serializer=StudentSerializer(pyolddata,data=pynewdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data is successfully updated"}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')  

    elif req.method=="DELETE":
        json_data=req.body
        if json_data:
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            x=pythondata['id']
            data = Student.objects.filter(id=x)
            if data : 
                showdata=Student.objects.get(id=x)
                showdata.delete()
                res={'msg':"Data is successfully Delete"}
                jsondata=JSONRenderer().render(res)
                return HttpResponse(jsondata,content_type='application/json')
            else :
                res={'msg':"Data is not found"}
                jsondata=JSONRenderer().render(res)
                return HttpResponse(jsondata,content_type='application/json')
