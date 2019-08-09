'''Zawiera zmienne konfiguracyjne do importowania w innych modułach.'''

# Czcionki
import os
import sys
font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, "bold")
font12 = ('Arial 800', 12)
font12b = ('Arial 800', 12, "bold")

version = '1.0.3b'
developer_mail = False
build = True

# Ustawienia
entry_width = 27  # Szerokość entry
# Odbiorcy maila sprzedażowego
if developer_mail:
    odbiorcy_sprzedazowy = ['kacper0witas@gmail.com']
    bcc_rodo = ['administrator@bedekoderem.pl']
else:
    odbiorcy_sprzedazowy = ['patryk.smucerowicz@gpgoldwin.pl',
                            'kacper.witas@gpgoldwin.pl',
                            'justyna.sujkowska@gpgoldwin.pl',
                            'oliwia.zachar@gpgoldwin.pl']
    bcc_rodo = ['informacje@gpgoldwin.pl',
                'kacper.witas@gpgoldwin.pl']


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



if not build:
    ikona = resource_path('./pliki/ikona.gif')
    rodo = resource_path('./pliki/rodo.txt')
    goldwin = resource_path('./pliki/goldwin.png')
    pdf129 = resource_path('./pliki/oferta/129.pdf')
    pdf159 = resource_path('./pliki/oferta/159.pdf')
    pdf199 = resource_path('./pliki/oferta/199.pdf')
    pdfgoldwin = resource_path('./pliki/oferta/Goldwin.pdf')
    tresc = resource_path('./pliki/oferta/tresc.txt')

else:
    ikona = resource_path('ikona.gif')
    rodo = resource_path('rodo.txt')
    goldwin = resource_path('goldwin.png')
    pdf129 = resource_path('129.pdf')
    pdf159 = resource_path('159.pdf')
    pdf199 = resource_path('199.pdf')
    pdfgoldwin = resource_path('Goldwin.pdf')
    tresc = resource_path('tresc.txt')
