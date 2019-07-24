'''Główny moduł. '''

from login import Login  # okno logowania
from menu import Menu  # okno menu
from umowa import Umowa  # okno umowa
from config import konsultant  # dane konsultanta

login = Login('GOLDWIN', '300x200')  # tworzy okno logowania
dodatkowi = ['', '', '']  # resetuje dodatkowych odbiorców
konsultant.dodatkowi(dodatkowi)  # resetuje dodatkowych odbiorców

# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
while True:
    menu = Menu('GOLDWIN', '300x300')
    if konsultant.wybor == 1:
        print('Umowa')
        umowa = Umowa('Umowa', '800x300')
    elif konsultant.wybor == 2:
        print('Aneks')
    elif konsultant.wybor == 3:
        print('Sprawy nierozwiązane')
    elif konsultant.wybor == 4:
        print('Wypowiedzenie')
