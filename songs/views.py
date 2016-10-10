from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .tasks import send_notification_ratesound
from .models import Song, SongRate
from .serializers import SongSerializer, SongRateSerializer
from users.models import User
class SongsCrud(APIView):

    def get(self, request):
        return Response({})

    def post(self, request):
        """
        {
            "name": "Al final del serndero",
            "album": "El condor Herido",
            "artist": "Diomedes Diaz",
            "duration": 240,
            "creator": 11,
            "audio_path": "None"
        }
        :param request:
        :return:
        """
        print(request.data)
        serializer = SongSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        creator = User.objects.get(id=data["creator"])
        song_new = Song.objects.create(
                name=data['name'],
                album=data["album"],
                artist=data["artist"],
                duration=data["duration"],
                audio_path = data["audio_path"],
                creator=creator
        )
        song_new.save()
        return Response(song_new.serialize(), status=status.HTTP_201_CREATED)

class SongsRateCrud(APIView):

    def post(self, request):
        """
        {
            "user": 11,
            "song": 3,
            "rate": 4
        }
        :param request:
        :return:
        """
        serializer = SongRateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        user = User.objects.get(id=data["user"])
        song = Song.objects.get(id=data["song"])
        songr_new = SongRate.objects.create(user=user, song=song, rate=data["rate"])
        songr_new.save()
        send_notification_ratesound.delay(songr_new.user.id, songr_new.song.id, songr_new.rate)
        return Response(songr_new.serialize(), status=status.HTTP_201_CREATED)