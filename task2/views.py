from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# Классовое представление
class ClassView(TemplateView):
    template_name = 'second_task/class_view.html'

# Функциональное представление
def function_view(request):
    return render(request, 'second_task/function_view.html')
