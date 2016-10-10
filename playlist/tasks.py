from utilities import redis_conn
from rq.decorators import job

from utilities import sender_email

@job('default', connection=redis_conn)
def send_create_playlist(playlist):
    """
    Envia un Email de bienvenida a una persona cuando se registra
    :param email: ejemplo: mymail@gmail.com
    :return: SendGridHttpResponse
    """
    return sender_email.send_email(playlist.user.email, "PlayList Creada", "<h1>Tienes una Nueva PlayList {0}</h1>".format(playlist.name))