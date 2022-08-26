from .utils import Utils
import requests
import json

URL = 'https://restcountries.com/v2/all'
countryData = requests.get(URL)
countryData = json.loads(countryData.text[:])
print(countryData)

class CountryData(object):
    @classmethod
    def addCountry(cls, data):
        def country_flag(rowData):
            countries = []
            for pays in countryData:
                country.append({'name':pays['name'], 'flag':pays['flags']['png']})
                rowData['country'] = countries[Utils.randomizeCountry(countries)]['name']
                rowData['flag'] = countries[Utils.randomizeCountry(countries)]['flag']
                return rowData

        data = map(country_flag, data)
        return list(data)
