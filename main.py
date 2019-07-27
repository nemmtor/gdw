# -*- coding: utf-8 -*-
'''Główny moduł. '''

from login import Login  # okno logowania
from menu import Menu  # okno menu
from umowa import Umowa  # okno umowa
from config import konsultant, mailsender  # dane konsultanta

login = Login('Goldwin - login', '300x130')  # tworzy okno logowania
dodatkowi = ['', '', '']  # resetuje dodatkowych odbiorców
mailsender.dodatkowi(dodatkowi)  # resetuje dodatkowych odbiorców

# nie przejdzie dalej dopóki nie wpiszemy prawidłowego loginu/hasła
while True:
    menu = Menu('Goldwin - menu', '300x230')
    if konsultant.wybor == 1:
        umowa = Umowa('Goldwin - umowa', '800x400')
    elif konsultant.wybor == 2:
        pass
    elif konsultant.wybor == 3:
        pass
    elif konsultant.wybor == 4:
        pass
