from utilities import redis_conn, push_notification, algolia
from rq.decorators import job
from mymusic.constants import *


@job('default', connection=redis_conn)
def send_notification_ratesound(user_id, song_id, rate):
    """
    Envia una notificaion cuando se califica una cancion
    :param user_id: Usuario a notificar
    :param song_id: Cancion calificada
    :param rate: Calificacion data por el usuario
    :return:
    """
    return push_notification.send(PUSHER_USER_CHANNEL.format(user_id=user_id), PUSHER_RATE_SOUND, {
        song_id: song_id,
        rate: rate
    })

@job('default', connection=redis_conn)
def send_data_to_algolia(index, data):
    """
    Agrega un objeto a Algolia
    :param index: Nombre del indice a alimentar
    :param data: Diccionario Data a indexar
    :return: AlgoliaResponse
    """
    return algolia.save_object(index=index, data=data)