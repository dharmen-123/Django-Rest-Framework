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

import csv
def exportcsv(req):
    pass

def exportpdf(req):
    pass


# from django.shortcuts import render
# from django.http import HttpResponse
# from.models import Employee
# import openpyxl
# # Create your views here.
# def home(req):
#     return render(req,'home.html')   

# def export_excel(req):
#     print("Hello..........")
#     wkbk = openpyxl.Workbook()
#     wkst=wkbk.active
#     wkst.title = "Data" #Data is tab name in excel sheet
#     wkst.append(["id","Name","Email","City","salary"]) #headr row we are creating in excel worksheet
    
#     for i in Employee.objects.all():
#         wkst.append([i.id, i.name, i.email, i.city , i.salary])
#     #know preparing response
#     response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreedsheetml.sheet")
#     response["Content-Disposition"]= "attachment; filename=employee.xlsx" # emplyee is excel file predefine
#     wkbk.save(response)
#     return response

# import csv       
# def export_csv(req):
#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"]= "attachment; filename= data.csv"  # emplyee is excel file predefine   
#     writer= csv.writer(response)
#     writer.writerow(["id","Name","Email","City","salary"]) #header row we are creating in csv
#     for obj in Employee.objects.all():
#         writer.writerow([obj.id, obj.name, obj.email, obj.city , obj.salary])
#     return response


# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def export_pdf(req):
#     template_path = 'pdf_template.html'
#     data ={'records':Employee.objects.all().values()}
#     # load and render the html template
#     template = get_template(template_path)
#     html = template.render(data)

#     #create a response object and specific content_type as pdf
#     response = HttpResponse(content_type ='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename ="date.pdf"'

#     # create pdf

#     pisa_status = pisa.CreatePDF(html,dest=response)

#     if pisa_status.err:
#         return HttpResponse('We had some error <pre>' + html + '</pre>')
#     return response