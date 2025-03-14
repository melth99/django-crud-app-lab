from django.urls import path
from . import views # Import views to connect routes to view functions
from django.views.generic.edit import CreateView
from .models import Predator


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('predators/', views.index, name= 'index'),
    path('predators/create/', views.PredatorCreate.as_view(), name='predator-create'),
    path('predators/<int:predator_id>/', views.predator_detail , name='predator-detail')
]
