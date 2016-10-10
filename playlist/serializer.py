from .models import PlayList, PlayListSong
from rest_framework import serializers

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ('name', 'description', 'gender')

class PlayListSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListSong
        fields = ('song', 'list')