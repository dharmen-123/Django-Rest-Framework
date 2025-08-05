from django.shortcuts import render

from .models import Employee
import csv
import io

# Create your views here.


def upload(req):
    return render(req,'home.html')
    