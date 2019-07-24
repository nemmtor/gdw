'''Główny moduł. '''

from login import Login  # okno logowania
from menu import Menu  # okno menu
from umowa import Umowa  # okno umowa
from config import konsultant  # dane konsultanta
login = Login('GOLDWIN', '300x200')
dodatkowi = ['', '', '']
konsultant.dodatkowi(dodatkowi)
# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
print(konsultant.login)
print(konsultant.password)
print(konsultant.kto)
while True:
    menu = Menu('GOLDWIN', '300x300')
    if konsultant.wybor == 1:
        umowa = Umowa('Umowa', '800x300')
    elif konsultant.wybor == 2:
        print('Aneks')
    elif konsultant.wybor == 3:
        print('Sprawy nierozwiązane')
    elif konsultant.wybor == 4:
        print('Wypowiedzenie')
