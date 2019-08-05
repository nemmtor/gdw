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
login = Login('Goldwin - login', '300x130')


# Nieskończona pętla służąca do obsługi menu
while True:
    # Stwórz okno menu
    menu = Menu('Goldwin - menu', '300x230')
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
        menu_oferta = Menu_Oferta('Oferta', '300x230')
        if menu_oferta.wybor == 1:
            print("Pan")
        elif menu_oferta.wybor == 2:
            print("Pani")
        # mailsender.oferta()
