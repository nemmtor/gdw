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
from tresc_maila import stworz_body, stworz_subject, stworz_rodo, stworz_oferte
from server import server
import imaplib
from tkinter import messagebox  # popup message

# Odbiorcy
from config import bcc_rodo, odbiorcy_sprzedazowy

class Mailsender():
    '''Klasa Mail dla obiektu mailsender.
    Odpowiada za przechowywanie odbiorców, dodatkowych odbiorców,
    nazwy załącznika.'''

    def __init__(self):
        '''Tworzy listę odbiorców i dodatkowych odbiorców(sprzedażowy)'''
        self.odbiorcy = odbiorcy_sprzedazowy
        self.dod_odbiorcy = ['', '', '']
        self.zalacznik = ''

    def oferta(self, cena, plec, mail, root):
        # Dane do maila
        self.plec = plec
        self.cena = cena
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        msg['To'] = mail
        msg['Subject'] = 'Grupa Prawna Goldwin'
        msg["Date"] = formatdate(localtime=True)

        # Body
        msg.attach(MIMEText(stworz_oferte(self.plec), 'html'))

        # Załącznik
        attachment = open('pliki/oferta/Goldwin.pdf', 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        # TODO - basename = zmiennazwe()
        part.add_header('Content-Disposition',
                        "attachment; filename= " +
                        os.path.basename('Grupa Prawna Goldwin.pdf'))
        msg.attach(part)

        # Załącznik - oferta
        if self.cena == 129:
            attachment = open('pliki/oferta/129.pdf', 'rb')
        elif self.cena == 159:
            attachment = open('pliki/oferta/159.pdf', 'rb')
        elif self.cena == 199:
            attachment = open('pliki/oferta/199.pdf', 'rb')


        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= " +
                        os.path.basename('Oferta.pdf'))
        msg.attach(part)

        # Do servera
        server.zaloguj()
        server.smtp.send_message(msg)
        # Dodaj wiadomosc do folderu SENT
        self.dodaj_do_sent(msg)
        server.rozlacz()
        root.destroy()
        return True

    def wyslij_sprzedazowy(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        for adres in self.dod_odbiorcy:
            if adres != '':
                if adres not in self.odbiorcy:
                    self.odbiorcy.append(adres)
        msg['To'] = ', '.join(self.odbiorcy)
        msg['Subject'] = stworz_subject(konsultant.wybor)
        msg["Date"] = formatdate(localtime=True)

        msg.attach(MIMEText(stworz_body(), 'html'))
        try:
            attachment = open(self.zalacznik, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= " +
                            os.path.basename(self.zalacznik))
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
        msg['Bcc'] = ', '.join(bcc_rodo)
        msg.attach(MIMEText(stworz_rodo(), 'html'))

        # Do servera
        server.smtp.send_message(msg)

        # Dodaj wiadomosc do folderu SENT
        self.dodaj_do_sent(msg)

    def dodaj_do_sent(self, msg):
        server.imap.append('SENT', '\\Seen',
                           imaplib.Time2Internaldate(time.time()),
                           msg.as_string().encode('utf8'))


# Nowy obiekt
mailsender = Mailsender()
