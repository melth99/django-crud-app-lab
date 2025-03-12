from django.db import models
from django.urls import reverse
#In Django, reverse is a function that allows you to retrieve a
#URL using its name defined in your URL patterns. 
# Instead of hardcoding URLs, you can refer to them by their names,

# Create your models here.

ANIMAL_CLASS = (
        'mammal',
        'amphibian',
        'bird',
        'fish',
        'reptile'
)

DIET = (
    'Omnivore',
    'Herbivore',
    'Carnivore'
)

class Predator (models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("predator_detail", kwargs={"pk": self.pk}) #no predator detail yet

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    """ diet = models.CharField(
      
        choices=DIET,
        #default =
        )
    #prey = models.ForeignKey(Prey, on )
    
    
 """

    
class Prey (models.Model):
    
    
    def __str__(self):
        return self.name

