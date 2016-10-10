from django.db import models

from users.models import User

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    audio_path = models.TextField(default="")
    durantion = models.IntegerField(default=0)
    date_get = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.FloatField(default=0)

class SongRate(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(User)
    rate = models.IntegerField(default=1)