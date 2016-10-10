from django.conf.urls import url
from .views import PlayListCrud, PlayListSongCrud

urlpatterns = [
    url(r'^api/playlist/$', PlayListCrud.as_view()),
    url(r'^api/plsongs/$', PlayListSongCrud.as_view()),
]