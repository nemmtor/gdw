'''Moduł zawierający klasę i obiekt Konsultant(dane konsultanta)'''
import re

# RegEx
# Pobiera z maila wszystko do @ (włącznie z @)
mail_expr = re.compile(r'^(.*?)@')


class Konsultant():
    '''Klasa Pracownik dla obiektu konsultant,
    odpowiada za przechowywanie loginu, hasła, imienia i nazwiska.'''

    def __init__(self):
        pass

    def dane(self, login, password):
        '''Przechowuje login i pw z entry loginu
        Tworzy atrybut konsultant.kto = Imie Nazwisko,
        odpala się w momencie poprawnego zalogowania.'''
        # Przechowanie loginu i pw
        self.login = login
        self.password = password

        # Pobierz z loginu wszystko do @ włącznie z @
        # group 1 - bez @
        self.kto = re.search(mail_expr, self.login).group(1)

        # Oddzielenie słów przed i po kropce
        self.kto = self.kto.split('.')

        # Imie i nazwisko z dużej litery
        self.kto = list(map(str.capitalize, self.kto))

        # Złączenie imienia i nazwiska
        self.kto = ' '.join(self.kto)
        return True

    def menu(self, wybor):
        '''Sprawdza co zostało wybrane (1 z 4 opcji w menu)'''
        self.wybor = wybor


# Nowy obiekt
konsultant = Konsultant()
