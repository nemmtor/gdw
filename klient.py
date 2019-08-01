'''Moduł zawierający klasę i obiekt Klient(dane klienta).'''

class Klient():
    '''Klasa Klient dla obiektu klient,
    przechowuje jego wszystkie dane.'''
    def __init__(self):
        pass

    def stworz_klienta(self, imnaz, tel, datasprz, datawys,
                       cena_dl, mail, branza, pytania, dodatkowe,
                       rej_var, kor_var, dost_var,
                       rej, kor, dost, nierozw):
        '''Tworzy atrybuty - dane klienta, w oparciu o dane z entry.'''
        self.imnaz = imnaz
        self.tel = tel
        self.datasprz = datasprz
        self.datawys = datawys
        self.cena_dl = cena_dl
        self.mail = mail
        self.branza = branza
        self.pytania = pytania
        self.dodatkowe = dodatkowe
        self.rej_var = rej_var
        self.kor_var = kor_var
        self.dost_var = dost_var
        self.nierozw = nierozw

        # Jeżeli checkboxy odznaczone to pobierz adresy z entry
        if not self.rej_var:
            self.rej = rej
        if not self.kor_var:
            self.kor = kor
        if not self.dost_var:
            self.dost = dost


# Nowy obiekt
klient = Klient()
