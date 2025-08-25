from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
# Create your views here.
import openpyxl
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    return render(request,'home.html')

def exportpdf(request):
    cdata=datetime.now()
    date=cdata.strftime()
    templatepath='pdf.html'
    data=User.objects.get(id=2)
    detail={
        'name':data.name,
        'email':data.email,
        'number':data.number,
        'date':date,
        'city':data.city
    }
    template=get_template(templatepath)
    html=template.render(detail)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']="attachment;filename=Invoice.pdf"
    pisa_state=pisa.CreatePDF(html,data=response)
    
    return response