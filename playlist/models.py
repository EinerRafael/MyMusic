from django.db import models
from users.models import User
from songs.models import Song
# Create your models here.

class PlayList(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255)
    rate = models.FloatField(default=0)
    gender = models.CharField(max_length=150)
    is_public = models.BooleanField(default=False)

class PlayListSong(models.Model):
    song = models.ForeignKey(Song)
    list = models.ForeignKey(PlayList)