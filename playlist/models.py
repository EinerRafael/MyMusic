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

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'rate': self.rate,
            'gender': self.gender,
            'is_public': self.is_public,
            'user': self.user.serialize()
        }

class PlayListSong(models.Model):
    song = models.ForeignKey(Song)
    list = models.ForeignKey(PlayList)

    def serialize(self):
        return {
            'song': self.song.serialize()
        }