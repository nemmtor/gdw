'''Moduł zawierający klasę i obiekt Konsultant'''
import re
from config import mail_expr

class Konsultant():
    '''Klasa Pracownik dla obiektu konsultant,
    odpowiada za przechowywanie loginu, hasła, imienia i nazwiska.'''
    def __init__(self):
        pass

    def dane(self, login, password):
        '''Przechowuje login i pw
        Tworzy atrybut konsultant.kto = Imie Nazwisko'''
        # Przechowanie loginu i pw
        self.login = login
        self.password = password

        # Sprawdzenie regex
        self.kto = re.search(mail_expr, self.login).group(1)

        # Oddzielenie słów przed i po kropce
        self.kto = self.kto.split('.')

        # Z dużej litery
        self.kto = list(map(str.capitalize, self.kto))

        # Złączenie imienia i nazwiska
        self.kto = ' '.join(self.kto)

    def menu(self, wybor):
        '''Sprawdza co zostało wybrane (1 z 4 opcji w menu)'''
        self.wybor = wybor

konsultant = Konsultant()  # Tworzy konsultanta
