from django.shortcuts import render

# Create your views here.
def example_view(request):
    # path - my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')