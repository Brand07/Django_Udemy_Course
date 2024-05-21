from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")

def sports_view(request):
    return HttpResponse("Sports View")

def finance_view(request):
    return HttpResponse("Finance View")