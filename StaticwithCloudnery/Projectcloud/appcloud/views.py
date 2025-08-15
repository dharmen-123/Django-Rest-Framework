from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(req):
    alldata=Student.objects.all()
    return render(req,'home.html',{'data':alldata})

def form(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        cpassword=req.POST.get('confirm')
        image=req.FILES.get('image')
        video=req.FILES.get('video')
        if not Student.objects.filter(email=email).exists():
            Student.objects.create(
              name=name,
              email=email,
              password=password,
              cpassword=cpassword,
              image=image,
              video=video )
            msg='Thanks for register'
            return redirect('home',{'msg':msg})  
        else:
            # Handle duplicate email gracefully
            msg='Use other email'
            return render(req,'home.html',{'msg':msg})

    else:
        msg = 'please fill the form'
        return render(req,'home.html',{'msg':msg})