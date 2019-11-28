from rest_framework import generics, permissions

from poketeam.models import Pokemon
from poketeam.models.pokemon import Time
from poketeam.serializers import PokemonSerializer, TimeSerializer


class PokeList(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = ()

class TimeCreate(generics.CreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class TimeList(generics.ListAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = ()