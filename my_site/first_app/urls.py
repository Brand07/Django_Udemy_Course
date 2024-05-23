from django.urls import path
from . import views


# These are first app patterns

# Dynamic Routing
urlpatterns = [
    path('', views.simple_view) # domain.com/first_app

]