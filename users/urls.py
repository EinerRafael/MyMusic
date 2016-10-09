
from django.conf.urls import url
from .views import UsersCrud

urlpatterns = [
    url(r'^api/users/$', UsersCrud.as_view())
]