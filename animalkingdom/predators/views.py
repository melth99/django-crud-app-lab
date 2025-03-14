# main_app/views.py
# 12345
from django.shortcuts import render
from .models import Predator
from django.views.generic.edit import CreateView,   DeleteView, UpdateView
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
    return render(request, 'index.html', {'predators':predators})

def predator_detail(request, predator_id):
    predator = Predator.objects.get(id=predator_id)
    return render(request, 'predators/detail.html', {'predator':predator})

# main-app/views.py

class PredatorCreate(CreateView):
    model = Predator
    fields = '__all__'
    #success_url = '/predators/'

class PredatorDelete(DeleteView):
    model = Predator
    pk_url_kwarg = 'predator_id'
    success_url = '/predators/'
    
class PredatorUpdate(UpdateView):
    model = Predator
    pk_url_kwarg = 'predator_id'  
    fields = '__all__'








#https://pages.git.generalassemb.ly/modular-curriculum-all-courses/django-crud-app-cat-collector/django-templates/
#https://generalassembly.instructure.com/courses/733/assignments/16647?module_item_id=64402