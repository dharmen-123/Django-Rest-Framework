from django.shortcuts import render

# Create your views here.
import openpyxl
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    return render(request,'home.html')
    
def exportpdf(request):
    
    pass