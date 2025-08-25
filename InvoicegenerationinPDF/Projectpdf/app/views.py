from django.shortcuts import render
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
    template='pdf.html'
    data=User.objects

    pass