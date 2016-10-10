
from django.conf.urls import url
from .views import SongsCrud, SongsRateCrud

urlpatterns = [
    url(r'^api/songs/$', SongsCrud.as_view()),
    url(r'^api/songs/rate/$', SongsRateCrud.as_view())
]