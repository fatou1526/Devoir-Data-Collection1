from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory

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
    print('\n')
