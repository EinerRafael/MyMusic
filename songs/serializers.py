from .models import Song, SongRate
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'album', 'artist', 'duration', 'audio_path')

class SongRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRate
        fields = ('song', 'user', 'rate')