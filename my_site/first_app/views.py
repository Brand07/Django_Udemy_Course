from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404


# Create your views here

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page'
}

# Topic needs to be dynamically informed
def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "No page for that topic"
        raise Http404("404 GENERIC ERROR!")

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    result = num1 + num2
    return HttpResponse(str(result))

