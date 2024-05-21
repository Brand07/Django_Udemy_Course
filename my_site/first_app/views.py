from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page'
}
def simple_view(request):
    return HttpResponse("SIMPLE VIEW")

def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])