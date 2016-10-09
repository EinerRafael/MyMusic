from algoliasearch import algoliasearch
from mymusic import constants

class Algolia():

    def __init__(self):
        self.client = algoliasearch.Client