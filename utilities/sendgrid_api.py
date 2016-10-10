import sendgrid
from sendgrid.helpers import mail
from mymusic.constants import *

class SenderEmail():
    """
    Clase que nos permite enviar emails mediante el API  de SendGrid
    """
    def __init__(self):
        """
        Inicializa el API de SendGrid
        """
        self.sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    def send_email(self, recipient, subject, template):
        """
        Permite enviar email con una
        :param recipient:
        :param subject:
        :param template:
        :return:
        """
        to_email = mail.Email(recipient)
        from_email = mail.Email(SENDGRID_SENDER)
        content = mail.Content('text/html', template)
        message = mail.Mail(from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=message.get())
        return response