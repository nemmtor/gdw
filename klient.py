'''Moduł zawierający klasę i obiekt Klient(dane klienta).'''


class Klient():
    '''Klasa Klient dla obiektu klient,
    przechowuje jego wszystkie dane.'''

    def __init__(self):
        pass

    def stworz_adres(self, var):
        if var == 1:
            return(self.adr1)
        elif var == 2:
            return(self.adr2)
        elif var == 3:
            return(self.adr3)
        else:
            return(None)

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

        mail = mail.split()
        self.mail = ', '.join(mail)

        self.branza = branza
        self.pytania = pytania
        self.dodatkowe = dodatkowe
        self.rej_var = rej_var
        self.kor_var = kor_var
        self.dost_var = dost_var
        self.adr1 = adr1
        self.adr2 = adr2
        self.adr3 = adr3
        self.nierozw = nierozw

        if self.rej_var == self.kor_var and self.rej_var == self.dost_var:
            self.rodzajadresu = 'rejkordost'

        if self.rej_var == self.kor_var and self.rej_var != self.dost_var:
            self.rodzajadresu = 'rejkor'

        if self.rej_var != self.kor_var and self.rej_var == self.dost_var:
            self.rodzajadresu = 'rejdost'

        if self.rej_var != self.kor_var and self.kor_var == self.dost_var:
            self.rodzajadresu = 'kordost'

        if self.rej_var != self.kor_var and self.kor_var != self.dost_var and\
                self.rej_var != self.dost_var:
            self.rodzajadresu = 'osobne'

        self.rej = self.stworz_adres(self.rej_var)
        self.kor = self.stworz_adres(self.kor_var)
        self.dost = self.stworz_adres(self.dost_var)


# Nowy obiekt
klient = Klient()
