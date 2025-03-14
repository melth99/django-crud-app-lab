from django.urls import path
from . import views # Import views to connect routes to view functions
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Predator


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('predators/', views.index, name= 'index'),
    path('predators/create/', views.PredatorCreate.as_view(), name='predator-create'),
    path('predators/<int:predator_id>/', views.predator_detail , name='predator-detail'),
    path('predators/<int:predator_id>/delete/', views.PredatorDelete.as_view(), name='predator-delete'),
    path('predators/<int:predator_id>/update/', views.PredatorUpdate.as_view(), name='predator-update')
]
