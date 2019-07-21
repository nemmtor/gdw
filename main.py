'''Główny moduł. '''

from login_window import LoginWindow  # okno logowania
from pracownik import konsultant  # dane konsultanta

login = LoginWindow('GOLDWIN', '300x200')
# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
print(konsultant.login)
print(konsultant.kto)
