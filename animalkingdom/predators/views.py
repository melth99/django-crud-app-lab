# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses

from django.http import HttpResponse

# Define the home view function


class Predators:
    def __init__(self,name,diet,prey):
        self.name = name
        self.diet = diet
        self.prey = prey
        
        
predators = [
    Predators('hawk','carnivore','rat'),
    Predators('tiger','carnivore','gazelle'),
    Predators('cat','carnivore','mouse'),
    Predators('wolf', 'carnivore', 'bunny'),
    Predators('giraffe', 'herbivore', 'leaf'),
    Predators('human','omnivore','cow')
]


def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello Zoologists!</h1>')

def about(request):
   return render(request, 'about.html')

def index(request):
    return render(request, 'predators/index.html', {'predators':predators})








#https://pages.git.generalassemb.ly/modular-curriculum-all-courses/django-crud-app-cat-collector/django-templates/
#https://generalassembly.instructure.com/courses/733/assignments/16647?module_item_id=64402