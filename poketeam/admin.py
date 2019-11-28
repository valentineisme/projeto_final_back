from django.contrib import admin

from .models import Pokemon
from .models.pokemon import Time

admin.site.register(Pokemon)
admin.site.register(Time)