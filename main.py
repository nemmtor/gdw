'''Główny moduł. '''
# TODO - jak długo połączenie smtp/imap?
# Okna
from login import Login
from menu import Menu
from umowa import Umowa
# Obiekty
from konsultant import konsultant  # dane konsultanta
from mailsender import mailsender

# Stwórz okno logowania - przejdzie dalej po poprawnym logowaniu
login = Login('Goldwin - login', '300x130')

# Zresetuj dodatkowych odbiorców
dodatkowi = ['', '', '']
mailsender.dodatkowi(dodatkowi)

# Nieskończona pętla służąca do obsługi menu
while True:
    # Stwórz okno menu
    menu = Menu('Goldwin - menu', '300x230')
    # Umowa
    if konsultant.wybor == 1:
        umowa = Umowa('Goldwin - umowa', '800x400')
    # Sprawy nierozwiązane
    # TODO - sprawy nierozwiązane - checkbox w umowie
    elif konsultant.wybor == 2:
        pass
    # Aneks
    elif konsultant.wybor == 3:
        pass
    # Wypowiedzenie
    elif konsultant.wybor == 4:
        pass
