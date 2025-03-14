from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#In Django, reverse is a function that allows you to retrieve a
#URL using its name defined in your URL patterns. 
# Instead of hardcoding URLs, you can refer to them by their names,

# Create your models here.

ANIMAL_CLASS = (
    ('mammal', 'Mammal'),
    ('amphibian', 'Amphibian'),
    ('bird', 'Bird'),
    ('fish', 'Fish'),
    ('reptile','Reptile')
    )
DIET = (
    ('omnivore','Omnivore'),
    ('herbivore' ,'Herbivore'),
    ('carnivore','Carnivore'),
    ('N/A','N/A')
    )

class Predator (models.Model):


    name = models.CharField(max_length=50, default='Unknown')
    diet = models.CharField(max_length=50, choices = DIET, default = 'Herbivore')
    animal_class = models.CharField(max_length=50, choices = ANIMAL_CLASS, default='mammal')
    prey = models.CharField(max_length=50, default='Unknown!')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
      

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("predator-detail", kwargs={"predator_id": self.id}) #no predator detail yet
       # return reverse("predator-update")

class Prey(models.Model):
    name = models.CharField(max_length=50, default='Unknown')
    animal_class = models.CharField(max_length=50, choices = ANIMAL_CLASS, default='mammal')
    diet = models.CharField(max_length=50, choices = DIET, default = 'Herbivore')
    predator_of_prey = models.ForeignKey(Predator, on_delete=models.CASCADE, related_name='hunted_preys')
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.name} is a {self.animal_class} with a {self.diet} diet"




