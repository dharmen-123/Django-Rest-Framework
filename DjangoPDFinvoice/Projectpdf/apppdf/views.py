from django.shortcuts import render
from .models import Invoice
# Create your views here.
from django.http import HttpResponse
import openxyl


def home(req):
    return render(req,'home.html')

def exportxlsx(req):
    pass

import csv
def exportcsv(req):
    pass

def exportpdf(req):
    pass

