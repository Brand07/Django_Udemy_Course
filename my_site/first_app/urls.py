from django.urls import path
from . import views


# These are first app patterns

urlpatterns = [
    path('', views.simple_view),
]