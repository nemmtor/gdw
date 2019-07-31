'''Zawiera zmienne konfiguracyjne do importowania w innych modułach.'''

import re  # dla regex

# RegEx
mail_expr = re.compile(r'^(.*?)@')

# Czcionki
font10 = ('Arial 800', 10)
font10b = ('Arial 800', 10, "bold")
font12 = ('Arial 800', 12)
font12b = ('Arial 800', 12, "bold")

# Ustawienia
entry_width = 27  # szerokość entry
