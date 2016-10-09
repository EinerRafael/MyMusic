from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User as DUser
from utilities import sender_email

class UsersCrud(APIView):

    def get(self, request):
        """
        Lista todos los usuarios
        :param request:
        :return:
        """
        users = [user.serialize() for user in User.objects.all()]
        return Response(users)

    def post(self, request):
        """
        Almacena un usuario en la base de datos.
        La tabla de Auth_user tambien se adiciona.
        Ejemplo de un Solicitud:
        {
            "first_name": "Einer",
            "last_name": "Perez",
            "email": "some@mail.com",
            "password": "Linked",
            "image": "None"
        }
        :param request: Por defecto Django Request
        :return: Response Object Django
        """
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        password = request.data.get('password')
        request.data.pop('password', None)
        user_new = User.objects.create(**request.data)
        user_new.save()
        user_d = DUser.objects.create_user(user_new.email, user_new.email, password)
        user_d.last_name = user_new.last_name
        user_d.save()
        sender_email.send_email(user_new.email, "Bienvenido a MyMusic", "<h1>Bienvendio a My Music</h1>")
        return Response(user_new.serialize(), status=status.HTTP_201_CREATED)

