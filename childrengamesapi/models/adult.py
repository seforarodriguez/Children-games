from django.db import models
from django.contrib.auth.models import User

class Adult (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.IntegerField()
    game_options = models.ManyToManyField("Game", through="MyKidsGames", related_name="kids_games")