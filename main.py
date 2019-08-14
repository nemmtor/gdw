'''Główny moduł. '''
# Okna
from login import Login
from menu import Menu
from menu_oferta import Menu_Oferta
from menu_rodoskrypt import Rodo_Skrypt
from umowa import Umowa
# Obiekty
from konsultant import konsultant  # dane konsultanta
from mailsender import mailsender
from klient import klient


# Stwórz okno logowania - przejdzie dalej po poprawnym logowaniu
login = Login('Goldwin Mailsender')


# Nieskończona pętla służąca do obsługi menu
while True:
    klient.rej = ''
    klient.kor = ''
    klient.dost = ''
    mailsender.zalacznik = ''
    # Stwórz okno menu
    menu = Menu('Goldwin Mailsender')
    # Umowa
    if konsultant.wybor == 1:
        umowa = Umowa('Goldwin Mailsender')
    # # Aneks
    # elif konsultant.wybor == 2:
    #     pass
    # # Wypowiedzenie
    # elif konsultant.wybor == 3:
    #     pass

    # Mail z ofertą
    elif konsultant.wybor == 4:
        menu_oferta = Menu_Oferta('Goldwin Mailsender')
    elif konsultant.wybor == 5:
        rodo_skrypt = Rodo_Skrypt('Goldwin Mailsender')
