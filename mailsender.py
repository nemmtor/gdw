'''Moduł zawierający klasę i obiekt mailsender'''

# Obiekty
from klient import klient
from konsultant import konsultant

# Dla wysyłki maila
import os
import time
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from tresc_maila import stworz_body, stworz_subject, stworz_rodo
from server import server
import imaplib

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

    def wyslij_sprzedazowy(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        for adres in mailsender.dod_odbiorcy:
            if adres != '':
                if adres not in mailsender.odbiorcy:
                    mailsender.odbiorcy.append(adres)
        msg['To'] = ', '.join(mailsender.odbiorcy)

        msg['Subject'] = stworz_subject(konsultant.wybor)
        msg["Date"] = formatdate(localtime=True)

        msg.attach(MIMEText(stworz_body(), 'html'))
        try:
            attachment = open(mailsender.zalacznik, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= " +
                            os.path.basename(mailsender.zalacznik))
            msg.attach(part)

            # Do servera
            server.smtp.send_message(msg)

            # Dodaj wiadomosc do folderu SENT
            self.dodaj_do_sent(msg)
            return True
        except AttributeError:
            messagebox.showinfo('Error', 'Nie dodałeś załącznika.')

    def wyslij_rodo(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        msg['To'] = klient.mail

        msg['Subject'] = 'Grupa Prawna Goldwin'
        msg['Date'] = formatdate(localtime=True)
        msg['Bcc'] = 'administrator@bedekoderem.pl'
        msg.attach(MIMEText(stworz_rodo(), 'html'))

        # Do servera
        server.smtp.send_message(msg)

        # Dodaj wiadomosc do folderu SENT
        self.dodaj_do_sent(msg)

    def dodaj_do_sent(self, msg):
        # server.imap.starttls()
        server.imap.append('SENT', '\\Seen',
                         imaplib.Time2Internaldate(time.time()),
                         msg.as_string().encode('utf8'))

# Nowy obiekt
mailsender = Mailsender()
