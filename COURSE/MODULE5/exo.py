from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.bceao import CurrencyScrapper
import pandas as pd
import requests
import json
from libraries.apiCountry import CountryDonnees
"""
    4. Grace aux trois Factory, implémenter une méthode qui concatène tous les trois datas. C'est à dire:
	- Celui de CsvFactory
	- Celui de JsonFactory
	- Celui de HtmlFactory
"""
def concatener(data1, data2, data3):
    final_data = data1 + data2 + data3
    return final_data


# Question 6
    URL = 'https://restcountries.com/v2/all'
    countryData = requests.get(URL)
    countryData = json.loads(countryData.text[:])
    print(countryData)

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
    
    """- Ajouter une nouvelle entrée qui donnera la conversion en XOF
		- Ainsi on aura une entrée contenant la devise attribuée
		- Puis une entrée contenant la conversion en XOF via les données de la BCEAO
    """
    print(Utils.divider())
    currency = CurrencyScrapper.makeCurrencyList()
    currencyDataframe = pd.DataFrame(currency)
    print(currencyDataframe)
    global_data['Conversion en XOF']=0
    global_data['Conversion en XOF'] = global_data['Conversion en XOF'] \
        .apply(lambda x: Utils.conversionXOF(global_data, currencyDataframe))
    print(global_data)
    
    print(Utils.divider())
    """
    . Utiliser l'API FREE de countries
    - Chercher l'API countries sur le NET
	- Pour ajouter des pays de manière aléatoire dans une nouvelle entrée (Colonne)
	- Puis y joindre les flags de ces pays dans une nouvelle entrée
"""
    paysdata = CountryDonnees.addCountry(countryData)
    global_data = list(global_data)