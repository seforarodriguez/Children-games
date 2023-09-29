from django.db import models


class MyKidsGames(models.Model):
    kids_age = models.IntegerField()
    kidsgames = models.ForeignKey("Games", on_delete=models.CASCADE)
    requested_by = models.ForeignKey("Adult", on_delete=models.CASCADE)
    