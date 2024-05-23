from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here

def simple_view(reqeust):
    return render(request, 'first_app/example.html') #.html


