'''Moduł zawierający klasę i obiekt Klient(dane klienta).'''


class Klient():
    '''Klasa Klient dla obiektu klient,
    przechowuje jego wszystkie dane.'''

    def __init__(self):
        pass

    def stworz_adres(self, var):
        '''Sprawdza radiobuttony adresów, zwraca odpowiedni adres'''
        if var == 1:
            # Zwróć dane z entry1
            return(self.adr1)
        elif var == 2:
            # Zwróć dane z entry2
            return(self.adr2)
        elif var == 3:
            # Zwróć dane z entry3
            return(self.adr3)
        else:
            # Nie zwracaj nic
            return(None)

    def rodzaj_adresu(self):
        '''Sprawdza rodzaj adresu - zależnie od tego jak zaznaczono RB'''
        if self.rej_var == self.kor_var and self.rej_var == self.dost_var:
            rodzajadresu = 'rejkordost'

        elif self.rej_var == self.kor_var and self.rej_var != self.dost_var:
            rodzajadresu = 'rejkor'

        elif self.rej_var != self.kor_var and self.rej_var == self.dost_var:
            rodzajadresu = 'rejdost'

        elif self.rej_var != self.kor_var and self.kor_var == self.dost_var:
            rodzajadresu = 'kordost'

        elif self.rej_var != self.kor_var and\
                self.kor_var != self.dost_var and\
                self.rej_var != self.dost_var:
            rodzajadresu = 'osobne'
        # Zwróć rodzaj adresu
        return(rodzajadresu)

    def stworz_klienta(self, imnaz, tel, datasprz, datawys,
                       cena_dl, mail, branza, pytania, dodatkowe,
                       rej_var, kor_var, dost_var,
                       adr1, adr2, adr3, nierozw):
        '''Tworzy atrybuty - dane klienta, w oparciu o dane z entry.'''
        self.imnaz = imnaz
        self.tel = tel
        self.datasprz = datasprz
        self.datawys = datawys
        self.cena_dl = cena_dl

        # Dla spółek, gdzie jest więcej niż 1 adres mailowy
        mail = mail.split()
        self.mail = ', '.join(mail)

        self.branza = branza
        self.pytania = pytania
        self.dodatkowe = dodatkowe

        # Wszystko co związane z adresami
        #    Sprawdza jakie checkboxy zaznaczone
        self.rej_var = rej_var
        self.kor_var = kor_var
        self.dost_var = dost_var
        #   Przechowuje wartości entry adresów
        self.adr1 = adr1
        self.adr2 = adr2
        self.adr3 = adr3
        self.rodzajadresu = self.rodzaj_adresu()
        #   Zwraca odpowiedni adres zależnie co zaznaczone
        self.rej = self.stworz_adres(self.rej_var)
        self.kor = self.stworz_adres(self.kor_var)
        self.dost = self.stworz_adres(self.dost_var)

        self.nierozw = nierozw


# Nowy obiekt
klient = Klient()
