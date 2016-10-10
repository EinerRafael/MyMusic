from utilities import redis_conn
from rq.decorators import job

from utilities import sender_email

@job('default', connection=redis_conn)
def send_create_playlist(playlist):
    """
    Envia un Email cuando una playList Es creada
    :param playlist: <PlayListModel> Playlist datos
    :return: SendGridApi
    """
    return sender_email.send_email(playlist.user.email, "PlayList Creada", "<h1>Tienes una Nueva PlayList {0}</h1>".format(playlist.name))