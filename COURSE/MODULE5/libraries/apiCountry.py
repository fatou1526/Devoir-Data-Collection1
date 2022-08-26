from .utils import Utils

class CountryDonnees(object):
    @classmethod
    def addCountry(cls, data):
        def country_flag(rowData):
            countries = []
            for pays in data:
                countries.append({'name':pays['name'], 'flag':pays['flags']['png']})
                rowData['country'] = countries[Utils.randomizeCountry(countries)]['name']
                rowData['flag'] = countries[Utils.randomizeCountry(countries)]['flag']
                return rowData

        data = map(country_flag, data)
        return list(data)
