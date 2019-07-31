'''Moduł zawierający klasę i obiekt mailsender'''

class Mailsender():
    '''Klasa Mail dla obiektu mailsender.
    Odpowiada za przechowywanie odbiorców, dodatkowych odbiorców,
    nazwy załącznika.'''
    def __init__(self):
        '''Tworzy listę odbiorców'''
        self.odbiorcy = ['kacper0witas@gmail.com']

    def dodatkowi(self, odbiorcy):
        '''Tworzy listę dodatkowych odbiorców.'''
        self.dod_odbiorcy = odbiorcy

    def plik(self, zalacznik):
        '''Nazwa załącznika.'''
        self.zalacznik = zalacznik


mailsender = Mailsender()  # Tworzy maila
