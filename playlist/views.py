from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from users.models import User
from songs.models import Song
from .models import PlayList, PlayListSong
from .serializer import PlayListSerializer, PlayListSongSerializer
from .tasks import send_create_playlist

class PlayListCrud(APIView):

    def post(self, request):
        """
        {
            "user": 11,
            "name": "Vallenato Nuevo",
            "gender": "Vallenato",
            "description": ""
        }
        :param request:
        :return:
        """
        serializer = PlayListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        user = User.objects.get(id=data["user"])
        new_playlist = PlayList.objects.create(
            name=data['name'],
            description=data['description'],
            gender=data['gender'],
            user=user,
        )
        new_playlist.save()
        send_create_playlist.delay(new_playlist)
        return Response(new_playlist.serialize(), status=status.HTTP_201_CREATED)


class PlayListSongCrud(APIView):
    def post(self, request):
        """
        {
            "song": 9,
            "list": 1
        }
        :param request:
        :return:
        """
        serializer = PlayListSongSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        song = Song.objects.get(id=data["song"])
        list = PlayList.objects.get(id=data["list"])
        new_playlist_song = PlayListSong.objects.create(
            song=song,
            list=list
        )
        new_playlist_song.save()
        return Response(new_playlist_song.serialize(), status=status.HTTP_201_CREATED)

