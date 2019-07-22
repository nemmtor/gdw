'''Główny moduł. '''

from login_window import LoginWindow  # okno logowania
from menu_window import MenuWindow, wybor  # okno menu
from pracownik import konsultant  # dane konsultanta
import conf
login = LoginWindow('GOLDWIN', '300x200')
# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
print(konsultant.login)
print(konsultant.kto)
while True:
    menu = MenuWindow('GOLDWIN', '300x300')
    if konsultant.wybor == 1:
        print("Umowa")
    elif konsultant.wybor == 2:
        print("Aneks")
    elif konsultant.wybor == 3:
        print("Sprawy nierozwiązane")
    elif konsultant.wybor == 4:
        print("Wypowiedzenie")
