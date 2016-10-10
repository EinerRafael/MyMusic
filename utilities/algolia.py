from algoliasearch import algoliasearch
from mymusic.constants import *

class Algolia():
    """
    Clase para manejar la conexion a algolia
    """

    def __init__(self):
        """
        Inicializa el cliente algolia
        """
        self.client = algoliasearch.Client(ALGOLIA_APPID, ALGOLIA_APIKEY)

    def save_object(self, index, data):
        """
        Almacena un dato en un indice especifico creado en algolia
        :param index: Nombre del indice
        :param data: Dato a enviar
        :return: None
        """
        self.index = self.client.init_index(index)
        self.index.add_objects([data])

    def search(self, index, text):
        self.client = algoliasearch.Client(ALGOLIA_APPID, ALGOLIA_SEARCHKEY)
        self.index = self.client.init_index(index)
        return self.index.search(text)