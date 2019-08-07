'''Główny moduł. '''
# Okna
from login import Login
from menu import Menu
from menu_oferta import Menu_Oferta
from umowa import Umowa
# Obiekty
from konsultant import konsultant  # dane konsultanta
from mailsender import mailsender

# Stwórz okno logowania - przejdzie dalej po poprawnym logowaniu
login = Login('Goldwin - login', '200x100')


# Nieskończona pętla służąca do obsługi menu
while True:
    # Stwórz okno menu
    menu = Menu('Goldwin - menu', '200x150')
    # Umowa
    if konsultant.wybor == 1:
        umowa = Umowa('Goldwin - umowa', '800x400')
    # # Aneks
    # elif konsultant.wybor == 2:
    #     pass
    # # Wypowiedzenie
    # elif konsultant.wybor == 3:
    #     pass
    # Mail z ofertą
    elif konsultant.wybor == 4:
        menu_oferta = Menu_Oferta('Oferta', '300x250')
