from django.urls import path
from . import views


# These are first app patterns

# Dynamic Routing
urlpatterns = [
    # Path converter 'str' informs Django that
    # The topic will always be a string
    path('<str:topic>/', views.news_view),
    # Likewise, the topic will be an int.
    path('<int:num1>/<int:num2>', views.add_view)
]