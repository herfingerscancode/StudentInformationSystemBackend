from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser


def student_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)

