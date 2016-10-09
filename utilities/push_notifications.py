from pusher import pusher
from mymusic.constants import *

class push_notifications():

    def __init__(self):
        """
        Crea el cliente para el conexion a pusher
        """
        self.client = pusher.Pusher(
          app_id=PUSHER_APP_ID,
          key=PUSHER_APP_KEY,
          secret=PUSHER_APP_SECRET,
          ssl=PUSHER_APP_SSL
        )

    def send(self, channel, event, data):
        """
        Envia datos a un canal especifico y evento dado
        :param channel: Nombre del canal
        :param event: Nombre
        :param data:
        :return: None
        """
        self.client.trigger(channel, event, data)