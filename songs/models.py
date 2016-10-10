from django.db import models

from users.models import User

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    audio_path = models.TextField(default="")
    artist = models.CharField(max_length=150)
    duration = models.IntegerField(default=0)
    creator = models.ForeignKey(User)
    date_get = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.FloatField(default=0)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'album': self.album,
            'artist': self.artist,
            'audio_path': self.audio_path,
            'duration': self.duration
        }

class SongRate(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(User)
    rate = models.IntegerField(default=1)

    def serialize(self):
        return {
            'id': self.id,
            'song': self.song.serialize(),
            'user': self.user.serialize(),
            'rate': self.rate
        }