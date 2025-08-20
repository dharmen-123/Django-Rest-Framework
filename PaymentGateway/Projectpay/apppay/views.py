from django.shortcuts import render
import razorpay

# Create your views here.

def home(request):
    return render(request,'home.html')

def payment(request):
    pass

def paymenthandle(request):
    pass