'''Przechowuje dane servera smtp/imap, sprawdza połaczenie.'''


# Dla servera
import smtplib
import imaplib

# Obiekty
from konsultant import konsultant


class Server():
    def __init__(self):
        pass
        # '''Przechowuje dane serverów.'''
        # self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        # self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')

    def zaloguj(self):
        '''Loguje do serverów smtp oraz imap.'''
        # Robi to tylko raz przy logowaniu i zostawia zalogowanym
        try:
            self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
            self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')
            self.smtp.starttls()
            self.imap.starttls()
            self.smtp.login(konsultant.login, konsultant.password)
            self.imap.login(konsultant.login, konsultant.password)
            return True
        except (smtplib.SMTPAuthenticationError,
                TypeError):
            return False

    def rozlacz(self):
        self.smtp.quit()
        self.imap.logout()


server = Server()
