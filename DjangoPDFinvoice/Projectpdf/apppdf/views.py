from django.shortcuts import render
from .models import Invoice
# Create your views here.


def home(req):
    return render(req,'home.html')

def exportxlsx(req):
    pass


def exportcsv(req):
    pass


def exportpdf(req):
    pass

