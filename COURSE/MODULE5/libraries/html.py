import json
from .utils import Utils
from bs4 import BeautifulSoup


BASE_URL = 'C:/Users/user/Desktop/DIT/Devoir-Data-Collection1/COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'

# 1. Completer le code de HtmlFactory, afin de récupérer les données
class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    @classmethod
    def main(cls):
        # 1. Completer le code de HtmlFactory, afin de récupérer les données
        data = cls.openFile() 
        return data
    