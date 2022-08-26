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

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x
