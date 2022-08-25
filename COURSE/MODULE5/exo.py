from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
if __name__ == '__main__':
    print(Utils.divider())
    # Question 1 Recuperation des données html
    print(HtmlFactory.main())
    print('\n')
