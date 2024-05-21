from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page'
}

# Topic needs to be dynamically informed
def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    result = num1 + num2
    return HttpResponse(str(result))

