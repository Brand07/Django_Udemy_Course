from django.shortcuts import render

# Create your views here.
def example_view(request):
    # path - my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):

    my_var = {'first_name': 'Brandon', 'last_name':'Yates',
              'some_list' : [1,2,3], 'some_dict': {'inside_key': 'inside_value'}}

    return render(request, 'my_app/variable.html', context = my_var)