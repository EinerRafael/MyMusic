from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from users.models import User
from songs.models import Song
from .models import PlayList, PlayListSong
from .serializer import PlayListSerializer, PlayListSongSerializer
from .tasks import send_create_playlist

class PublicPlayList(APIView):
    """docstring for PublicPlayList"""
    def get(self, request):
        """
            Retorna todas plas playList Publicas
        """
        play_lists = [pl.serialize() for pl in PlayList.objects.filter(is_public=True)]
        if len(play_lists) is 0:
            return Response("", status=status.HTTP_404_NOT_FOUND)
        return Response(play_lists, status=status.HTTP_200_OK)
        

class PlayListCrud(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, BasicAuthentication)

    def post(self, request):
        """
        Permite adicionar una playList de un usuario.
        Ejemplo Solicitud:
        {
            "user": 11,
            "name": "Vallenato Nuevo",
            "gender": "Vallenato",
            "description": "",
            "is_public": 0
        }
        :param request: Objeto Request por defecto de DJango Restfrawmework
        :return: Object Respuesta de Django Restfrawmework
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
            is_public=data['is_public']
        )
        new_playlist.save()
        send_create_playlist.delay(new_playlist)
        return Response(new_playlist.serialize(), status=status.HTTP_201_CREATED)


class PlayListGet(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, BasicAuthentication)

    def get(self, request, id):
        """
        Adquiere un playlist con id especifico
        :param request: Objeto Request por defecto de DJango Restfrawmework
        :param id: Identificador de la PlayList
        :return: Object Respuesta de Django Restfrawmework
        """
        play_list = PlayList.objects.filter(id=int(id))
        if len(play_list) is 0:
            return Response("", status=status.HTTP_404_NOT_FOUND)
        return Response(play_list[0].serialize(), status=status.HTTP_200_OK)

class PlayListUser(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, BasicAuthentication)

    def get(self, request, id):
        """
        Adquiere un playlist con id de usuario especifico
        :param request: Objeto Request por defecto de DJango Restfrawmework
        :param id: Identificador del usuario
        :return: Object Respuesta de Django Restfrawmework
        """
        play_lists = [pl.serialize() for pl in PlayList.objects.filter(user=int(id))]
        if len(play_lists) is 0:
            return Response("", status=status.HTTP_404_NOT_FOUND)
        return Response(play_lists, status=status.HTTP_200_OK)


class PlayListSongCrud(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, BasicAuthentication)

    def post(self, request):
        """
        Permite adiconar una cacion a una playlist.
        Ejemplo Solicitud:
        {
            "song": 9,
            "list": 1
        }
        :param request: Objeto Request por defecto de DJango Restfrawmework
        :return: Object Respuesta de Django Restfrawmework
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

