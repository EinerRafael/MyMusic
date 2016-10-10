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

from django.conf.urls import url, include
from django.contrib import admin

# Rest Framework Mapping
from rest_framework import routers

##Import Views
router = routers.DefaultRouter()
#router.register(r'users', views.UsersView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('users.urls', namespace='users'))
]

"""
curl -H 'Accept: application/json; indent=4' -u john:johnpassword http://127.0.0.1:8080/api/users/
"""