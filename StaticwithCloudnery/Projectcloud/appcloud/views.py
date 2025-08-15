from django.shortcuts import render
from .models import Student
# Create your views here.

def home(req):
    
    return render(req,'home.html')

def form(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        cpassword=req.POST.get('confirm')
        image=req.FILES.get('image')
        video=req.FILES.get('video')
        Student.objects.create(name=name,email=email,password=password,cpassword=cpassword,image=image,video=video)
        msg = 'thanks'
        return render(req,'home.html',{'msg':msg})

    else:
        msg = 'please fill the form'
        return render(req,'home.html',{'msg':msg})