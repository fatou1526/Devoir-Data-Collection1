import random


class Utils(object):
    @classmethod
    def divider(cls, n=54):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)
            
    # Cette methode sera utilisée pour attribuer aléatoirement le type de monnaies entre Euro, Dollar et Yen       
    @classmethod
    def randomizeCurrency(cls,
                          liste:list()):
        return random \
            .choice(liste)
         
    # Cette methode sera utilisée pour faire la conversion XOF des devises   
    @classmethod 
    def conversionXOF(cls, dataframe1, dataframe2):
        for i in range(len(dataframe2)):
            for j in range(len(dataframe1)):
                if dataframe1['Devise'][j] == dataframe2['Devise'][i]:
                    dataframe1['Conversion en XOF'][j] = float(dataframe1['salary'][j]) * float(dataframe2['Achat'][i])
        return dataframe1
    
    # Question 6: Cette methode sera utilisé pour assigner aléatoirement les pays
    @classmethod
    def randomizeCountry(cls, liste):
        return random\
            .randint(0, len(liste)-1)

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x
