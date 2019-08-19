'''Zawiera elementy którę są importowane w wielu modułach.'''

# dla odpowiedniego dodania plikow do wersji exe
import os
import sys
# dla ustawienia daty
import datetime


version = '1.0.7.0'
developer_mail = True
build = Fale


# Ustawienia
#   Czcionki
font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, 'bold')
font12 = ('Arial 800', 12)
font12b = ('Arial 800', 12, 'bold')
#   Regex dla sprawdzania poprawności maila
mail_regex = r'.+@.+\..+'
#   Szerokość entry
entry_width = 33
#   Odbiorcy maila sprzedażowego
#       Jeżeli jest włączona opcja developer
if developer_mail:
    odbiorcy_sprzedazowy = ['kacper0witas@gmail.com']
    bcc_rodo = ['administrator@bedekoderem.pl']
#       Jeżeli normalni odbiorcy
else:
    odbiorcy_sprzedazowy = ['patryk.smucerowicz@gpgoldwin.pl',
                            'kacper.witas@gpgoldwin.pl',
                            'justyna.sujkowska@gpgoldwin.pl',
                            'oliwia.zachar@gpgoldwin.pl']
    bcc_rodo = ['informacje@gpgoldwin.pl',
                'kacper.witas@gpgoldwin.pl']

# Funkcje
#   Data


def czy_dodac_0(num):
    '''Funkcja sprawdza czy podany numer ma długość 1, jeżeli tak: dopisz 0.'''
    if len(num) == 1:
        num = f'0{num}'
    return(num)


def stworz_date(kiedy):
    'Tworzy date dzisiejszą/jutrzejszą zależnie od argumentu.'
    if kiedy == 'dzis':
        # Pobierz dzien, miesiac, rok i wrzuc do strina
        dzien = str(datetime.datetime.now().day)
        miesiac = str(datetime.datetime.now().month)
        rok = str(datetime.datetime.now().year)
    # Sprawdz czy dopisac 0, dla formatu DD.MM.YY
    dzien = czy_dodac_0(dzien)
    miesiac = czy_dodac_0(miesiac)
    # Zwróć date w postaci DD.MM.YY
    data = f'{dzien}.{miesiac}.{rok}'
    return(data)


#   Dla odpowiedniego dodania plików do wersji exe
def resource_path(relative_path):
    '''Get absolute path to resource, works for dev and for PyInstaller.'''
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)


if not build:
    ikona = resource_path('./pliki/ikona.gif')
    rodo = resource_path('./pliki/rodo.txt')
    rodoinf = resource_path('./pliki/rodoinf.txt')
    goldwin = resource_path('./pliki/goldwin.png')
    pdf129 = resource_path('./pliki/oferta/129.pdf')
    pdf159 = resource_path('./pliki/oferta/159.pdf')
    pdf199 = resource_path('./pliki/oferta/199.pdf')
    pdfgoldwin = resource_path('./pliki/oferta/Goldwin.pdf')
    tresc = resource_path('./pliki/oferta/tresc.txt')

else:
    ikona = resource_path('ikona.gif')
    rodo = resource_path('rodo.txt')
    rodoinf = resource_path('rodoinf.txt')
    goldwin = resource_path('goldwin.png')
    pdf129 = resource_path('129.pdf')
    pdf159 = resource_path('159.pdf')
    pdf199 = resource_path('199.pdf')
    pdfgoldwin = resource_path('Goldwin.pdf')
    tresc = resource_path('tresc.txt')
