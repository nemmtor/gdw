'''Dane dostępne we wszystkich modułach.'''

import re

# Czcionki
font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, "bold")
font12 = ('Arial 800', 12)
font12b = ('Arial 800', 12, "bold")

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
        self.kto = ' '.join(self.kto)  # łączy imie i nazwisko

    def menu(self, wybor):
        '''Sprawdza co zostało wybrane (1 z 4 opcji w menu)'''
        self.wybor = wybor


class Mail():
    def __init__(self):
        self.odbiorcy = ['kacper0witas@gmail.com']

    def dodatkowi(self, odbiorcy):
        self.dod_odbiorcy = odbiorcy

    def plik(self, zalacznik):
        '''Załącznik wybrany przez konsultanta!'''
        self.zalacznik = zalacznik


class Klient():
    def __init__(self):
        pass

    def stworz_klienta(self, imnaz, tel, datasprz, datawys,
                       cena_dl, mail, branza, pytania, dodatkowe,
                       rej_var, kor_var, dost_var,
                       rej, kor, dost):
        self.imnaz = imnaz
        self.tel = tel
        self.datasprz = datasprz
        self.datawys = datawys
        self.cena_dl = cena_dl
        self.mail = mail
        self.branza = branza
        self.pytania = pytania
        self.dodatkowe = dodatkowe
        if not rej_var:
            self.rej = rej
        if not kor_var:
            self.kor = kor
        if not dost_var:
            self.dost = dost


konsultant = Pracownik('', '')  # Tworzy konsultanta
mailsender = Mail()  # Tworzy maila
klient = Klient()
