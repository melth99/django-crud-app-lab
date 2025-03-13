# main_app/views.py

from django.shortcuts import render
from .models import Predator

# Import HttpResponse to send text-based responses

from django.http import HttpResponse

# Define the home view function



def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello Zoologists!</h1>')

def about(request):
   return render(request, 'about.html')

def index(request):
    predators = Predator.objects.all()
    return render(request, 'predators/index.html', {'predators':predators})








#https://pages.git.generalassemb.ly/modular-curriculum-all-courses/django-crud-app-cat-collector/django-templates/
#https://generalassembly.instructure.com/courses/733/assignments/16647?module_item_id=64402