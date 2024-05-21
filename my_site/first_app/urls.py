from django.urls import path
from . import views


# These are first app patterns

urlpatterns = [
    path('', views.simple_view),
    path('sports/', views.sports_view),
    path('finance/', views.finance_view)

]