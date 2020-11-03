
"""Game DB Model Module"""
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from ..models import Gamer

class Game(models.Model):
    """Representation of a game that a gamer can create"""
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name="games")
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()