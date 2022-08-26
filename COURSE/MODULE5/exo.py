from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.bceao import CurrencyScrapper
import pandas as pd
"""
    4. Grace aux trois Factory, implémenter une méthode qui concatène tous les trois datas. C'est à dire:
	- Celui de CsvFactory
	- Celui de JsonFactory
	- Celui de HtmlFactory
"""
def concatener(data1, data2, data3):
    final_data = data1 + data2 + data3
    return final_data
if __name__ == '__main__':
    print(Utils.divider())
    # Question 1, 2 et 3: Recuperation et affichage des données html
    print(HtmlFactory.main())
    print(Utils.divider())
    # Question 4: Concaténation des bases de données Html, Csv et Json
    global_data = concatener(HtmlFactory.main(),CsvFactory.main(),JsonFactory.main())
    print(global_data)
    
    print(Utils.divider())
    """5. Utiliser le lien de la BCEAO concernant les devises:
	- Ajouter une nouvelle entrée dans la donnée globale
	- Puis cette entrée doit contenir (Euro, Dollar, Yen)
	- Attribuer de manière aléatoire ces Devises
	- Grace aux données collecter via Scrapping du site de la BCEAO concernant les devises
    """
    print(CurrencyScrapper.makeCurrencyList())
    print(Utils.divider())
    global_data = pd.DataFrame(global_data)
    global_data['Devise']=""
    global_data['Devise'] = global_data['Devise'] \
        .apply(lambda x: Utils.randomizeCurrency(['Euro', 'Dollar us', 'Yen japonais']))
    print(global_data)
