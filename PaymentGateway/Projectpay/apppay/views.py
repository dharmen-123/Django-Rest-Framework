from django.shortcuts import render
import razorpay

# Create your views here.

def home(request):

    return render(request,'home.html')

def payment(request):
    if request.method=='POST':
        amount=request.POST.get('amount')*100
        client=razorpay.Client(auth=("rzp_test_8MpcoTaUXnGlMQ","wz2Q1xWs4LueA8LZwxIBMuPR"))
        order_data={
            'amount':amount,
            'currency':'INR',
            'receipt':"order_rcptid_11",
            'payment_capture':1
        }
        order=client.order.create(data=order_data)
        payment = {
            "order_id": order["id"],
            "amount": amount,
            "razorpay_key":"rzp_test_8MpcoTaUXnGlMQ" ,
            "currency": "INR",
            "callback_url": "/paymenthandle/"
        }    
        return render(request,'home.html',{'payment':payment})    
    return render(request,'home.html')
    
def paymenthandle(request):
    pass