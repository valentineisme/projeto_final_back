from django.db import transaction
from rest_framework import serializers
from .models import (Pokemon)
from .models.pokemon import Time

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'nome', 'tipo1', 'tipo2')

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'user', 'pokemon')