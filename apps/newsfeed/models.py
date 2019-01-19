from django.db import models
from apps.races.models import Race

# Create your models here.
class FeedItem(models.Model):
    hed=models.CharField(max_length=280)
    link=models.CharField(max_length=1000)
    races=models.ManyToManyField(Race)
    def __str__(self):
        return self.hed

"""
class RaceTag(models.Model):
    item = models.ForeignKey(FeedItem,on_delete=models.CASCADE)
    race = models.ForeignKey(Race,on_delete=models.CASCADE)
"""
