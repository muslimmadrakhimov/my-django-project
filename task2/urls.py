from django.urls import path
from .views import function_view, ClassView


urlpatterns = [
    path('class/', ClassView.as_view(), name='class_view'),
    path('function/', function_view, name='function_view'),
]