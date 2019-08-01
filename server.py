'''Przechowuje dane servera smtp/imap, sprawdza połaczenie.'''

from tkinter import messagebox  # popup message

# Dla servera
import smtplib
import imaplib

# Obiekty
from konsultant import konsultant

class Server():
    def __init__(self):
        '''Przechowuje dane serverów.'''
        self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')


    # def zaloguj(self):
    #     '''Loguje do serverów smtp oraz imap.'''
    #     try:
    #         self.smtp.starttls()
    #         self.smtp.login(konsultant.login, konsultant.password)
    #         # self.imap.starttls()
    #         # self.imap.login(konsultant.login, konsultant.password)
    #         return True
    #     except (smtplib.SMTPAuthenticationError,
    #             TypeError):
    #         return False

    def zaloguj(self):
        # self.smtp.starttls()
        self.smtp.login(konsultant.login, konsultant.password)
        self.imap.login(konsultant.login, konsultant.password)
        return True


server = Server()
