'''Dane konsultanta globalne, dostępne z każdego innego modułu.
konsultant.kto = Imie Nazwisko
'''

import re

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


konsultant = Pracownik('', '')
