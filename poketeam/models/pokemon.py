from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    nome = models.CharField(max_length=128, null=False)
    tipo1 = models.CharField(max_length=128, null=False)
    tipo2 = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return self.nome

class Time(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (self.pokemon.nome)
