from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Predator
from .models import Prey

admin.site.register(Prey)

admin.site.register(Predator)