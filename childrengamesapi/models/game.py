from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=350)
    description = models.CharField(max_length=350)