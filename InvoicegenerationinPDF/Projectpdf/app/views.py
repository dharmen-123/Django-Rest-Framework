from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from .models import User
import io
# Create your views here.
import openpyxl
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    return render(request,'home.html')

def exportpdf(request):
    cdata=datetime.now()
    date=cdata.strftime("%B %d ,%Y")
    data=User.objects.get(id=2)
    detail={
        'name':data.name,
        'email':data.email,
        'number':data.number,
        'date':date,
        'city':data.city
    }
    templatepath='pdf.html'
    template=get_template(templatepath)
    html=template.render(detail)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), dest=result)   
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Invoice.pdf"'
        return response
    else:
        return HttpResponse("Error generating PDF", status=500)

