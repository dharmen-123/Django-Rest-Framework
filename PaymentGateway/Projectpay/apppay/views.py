from django.shortcuts import render
import razorpay
from .models import Payment
# Create your views here.

def home(request):
    return render(request,'home.html')

def payment(request):
    if request.method=='POST':
        amount=int(2000*100)
        client=razorpay.Client(auth=("rzp_test_8MpcoTaUXnGlMQ","wz2Q1xWs4LueA8LZwxIBMuPR"))
        order_data={
            'amount':amount,
            'currency':'INR',
            'receipt':"order_rcptid_11",
            'payment_capture':1
        }
        order=client.order.create(data=order_data)
        Payment.objects.create(
            order_id=order["id"],
            amount=amount,
            status="Created"
            )
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
    if request.method=='POST':
        client = razorpay.Client(auth=("rzp_test_8MpcoTaUXnGlMQ", "wz2Q1xWs4LueA8LZwxIBMuPR"))
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }
        # Verify the payment signature
        client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(order_id=request.POST.get('razorpay_order_id'))
        payment.payment_id = request.POST.get('razorpay_payment_id')
        payment.signature = request.POST.get('razorpay_signature')
        payment.status = "Paid"
        payment.save()
        return render(request,'home.html',{'success':1})