from django.shortcuts import render,redirect

from .models import Employee
import csv
import io

# Create your views here.


def upload(req):
    if req.method=='POST':
        csvfile=req.FILES['csvfile']
        decoded_file=csvfile.read().decode('utf-8')
        iostring=io.StringIO(decoded_file)
        reader=csv.DictReader(iostring)
        for row in reader:
            Employee.objects.create(
                name=row['name'],
                email=row['email'],
                contact=row['contact'],
                department=row['department'],
                salary=row['salary'],
            )
        return render(req,'home.html')
    else:
        return render(req,'home.html')
