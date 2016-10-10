from django.conf.urls import url
from .views import PlayListCrud, PlayListSongCrud, PlayListGet,PlayListUser

urlpatterns = [
    url(r'^api/playlist/$', PlayListCrud.as_view()),
    url(r'^api/playlist/(?P<id>\d+)/$$', PlayListGet.as_view()),
    url(r'^api/playlist/user/(?P<id>\d+)/$$', PlayListUser.as_view()),
    url(r'^api/plsongs/$', PlayListSongCrud.as_view()),
]