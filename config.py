'''Dane konsultanta globalne, dostępne z każdego innego modułu.
konsultant.kto = Imie Nazwisko
'''

import re

font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, "bold")

entry_width = 27



expr = re.compile(r'^(.*?)@')


class Pracownik():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def dane(self, login, password):
        '''Tworzy atrybut /kto/ czyli Imie Nazwisko '''
        self.kto = re.search(expr, self.login).group(1)
        self.kto = self.kto.split('.')
        self.kto = list(map(str.capitalize, self.kto))
        self.kto = ' '.join(self.kto)

    def menu(self, wybor):
        self.wybor = wybor

    def dodatkowi(self, odbiorcy):
        self.dod_odbiorcy = odbiorcy


konsultant = Pracownik('', '')
