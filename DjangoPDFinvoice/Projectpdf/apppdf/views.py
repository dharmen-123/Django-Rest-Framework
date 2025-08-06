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
    wb.append(["ID","Name","Email","DOB","Contact","City","Price"])
    for i in Invoice.objects.all():
        wb.append([i.id,i.name,i.email,i.dob,i.contact,i.city,i.price])

    response=HttpResponse(content_type="application/vnd.openxmlformats-officedocuments.spreedsheetml.sheet")
    response('Content-Disposition',"attachment")
    wb.save(response)
    return response
    pass

import csv
def exportcsv(req):
    pass


def exportpdf(req):
    pass

