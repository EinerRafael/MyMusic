from utilities import redis_conn
from rq.decorators import job

from utilities import sender_email

@job('default', connection=redis_conn)
def send_welcome_email(email):
    """
    Envia un Email de bienvenida a una persona cuando se registra
    :param email: ejemplo: mymail@gmail.com
    :return: SendGridHttpResponse
    """
    return sender_email.send_email(email, "Bienvenido a MyMusic", "<h1>Bienvendio a My Music</h1>")