'''Główny moduł. '''

from login import Login  # okno logowania
from menu import Menu  # okno menu
from umowa import Umowa  # okno umowa
from pracownik import konsultant  # dane konsultanta
login = Login('GOLDWIN', '300x200')
# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
print(konsultant.login)
print(konsultant.password)
print(konsultant.kto)
while True:
    menu = Menu('GOLDWIN', '300x300')
    if konsultant.wybor == 1:
        print('Umowa')
        nowa = Umowa('Umowa','300x500')
    elif konsultant.wybor == 2:
        print('Aneks')
    elif konsultant.wybor == 3:
        print('Sprawy nierozwiązane')
    elif konsultant.wybor == 4:
        print('Wypowiedzenie')
