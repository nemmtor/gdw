'''Dane dostępne we wszystkich modułach.'''

import re

# Czcionki
font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, "bold")

# Ustawienia
entry_width = 27  # szerokość entry

# Regex
expr = re.compile(r'^(.*?)@')  # Regex dla maila


# Obiekty
class Pracownik():
    def __init__(self, login, password):
        '''Przechowuje login i pw.'''
        self.login = login
        self.password = password

    def dane(self, login, password):
        '''Tworzy atrybut /kto/
        konsultant.kto = Imie Nazwisko'''
        self.kto = re.search(expr, self.login).group(1)  # używa regex
        self.kto = self.kto.split('.')  # splituje liste (.)
        self.kto = list(map(str.capitalize, self.kto))  # capitalizuje liste
        self.kto = ' '.join(self.kto)  #  łączy imie i nazwisko

    def menu(self, wybor):
        '''Sprawdza co zostało wybrane (1 z 4 opcji w menu)'''
        self.wybor = wybor

    def dodatkowi(self, odbiorcy):
        '''Przenieść do klasy Mail.'''
        self.dod_odbiorcy = odbiorcy

# class Mail():
#     def __init__(self):
#         pass
#     def dodatkowi(self, odbiorcy):
#         self.odbiorcy = odbiorcy

konsultant = Pracownik('', '')  # Tworzy konsultanta
