"""mymusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

# Rest Framework Mapping
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^web/', include('web.urls')),
    url(r'', include('users.urls', namespace='users')),
    url(r'', include('songs.urls', namespace='songs')),
    url(r'', include('playlist.urls', namespace='playlist'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
curl -X POST -d "username=einper40@gmail.com&password=Linked" http://localhost:8080/auth-token/
"""