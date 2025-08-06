from django.shortcuts import render , redirect
from .models import Invoice
from django.http import HttpResponse
import openpyxl

def home(req):
    return render(req,'home.html')


def exportxlsx(req):
    wb=openpyxl.Workbook()
    wb=wb.active
    wb.title="Data"
    pass

import csv
def exportcsv(req):
    pass


def exportpdf(req):
    pass

