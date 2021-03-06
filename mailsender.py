'''Moduł zawierający klasę i obiekt mailsender'''

# Obiekty
from klient import klient
from konsultant import konsultant

# Dla wysyłki maila
import os
import time
from email import encoders
from email.utils import formatdate, formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from tresc_maila import stworz_body, stworz_subject, stworz_rodo
from tresc_maila import stworz_oferte, stworz_rodoinf
from server import server
import imaplib
from tkinter import messagebox  # popup message

# Odbiorcy
import re
from config import bcc_rodo, odbiorcy_sprzedazowy
from config import pdf129, pdf159, pdf199, pdfgoldwin
from config import mail_regex


class Mailsender():
    '''Klasa Mail dla obiektu mailsender.
    Odpowiada za przechowywanie odbiorców, dodatkowych odbiorców,
    nazwy załącznika.'''

    def __init__(self):
        '''Tworzy listę odbiorców i dodatkowych odbiorców(sprzedażowy)'''
        self.odbiorcy = odbiorcy_sprzedazowy
        self.dod_odbiorcy = ['', '', '']
        self.zalacznik = ''

    def rodo_inf(self, mail, root):
        if re.match(mail_regex, mail):
            msg = MIMEMultipart('mixed')
            msg['From'] = formataddr(
                (str(Header(konsultant.kto, 'utf-8')), konsultant.login))
            msg['To'] = mail
            msg['Subject'] = 'Grupa Prawna Goldwin'
            msg["Date"] = formatdate(localtime=True)

            # Body
            msg.attach(MIMEText(stworz_rodoinf(), 'html'))

            # Do servera
            server.zaloguj()
            server.smtp.send_message(msg)
            # Dodaj wiadomosc do folderu SENT
            self.dodaj_do_sent(msg)
            server.rozlacz()
            messagebox.showinfo(
                'Wysłano', 'Wysłano maila informacyjnego z RODO.')
            root.destroy()
            return True
        else:
            messagebox.showinfo('Error', 'Błędny adres mailowy!')

    def oferta(self, cena, plec, mail, root):
        # Dane do maila
        if re.match(mail_regex, mail):
            self.plec = plec
            self.cena = cena
            msg = MIMEMultipart('mixed')
            msg['From'] = formataddr(
                (str(Header(konsultant.kto, 'utf-8')), konsultant.login))
            msg['To'] = mail
            msg['Subject'] = 'Grupa Prawna Goldwin'
            msg["Date"] = formatdate(localtime=True)

            # Body
            msg.attach(MIMEText(stworz_oferte(self.plec, self.cena), 'html'))

            # Załącznik
            attachment = open(pdfgoldwin, 'rb')
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
                attachment = open(pdf129, 'rb')
            elif self.cena == 159:
                attachment = open(pdf159, 'rb')
            elif self.cena == 199:
                attachment = open(pdf199, 'rb')

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
            messagebox.showinfo('Wysłano', 'Wysłano maila z ofertą')
            root.destroy()
            return True
        else:
            messagebox.showinfo('Error', 'Błędny adres mailowy!')

    def wyslij_sprzedazowy(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = formataddr(
            (str(Header(konsultant.kto, 'utf-8')), konsultant.login))
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
                            os.path.basename('zalacznik.'
                                             + self.zalacznik.split('.')[-1]))
            msg.attach(part)

            # Do servera
            server.smtp.send_message(msg)

            # Dodaj wiadomosc do folderu SENT
            self.dodaj_do_sent(msg)
            return True
        except (AttributeError and FileNotFoundError):
            messagebox.showinfo('Error', 'Nie dodałeś załącznika.')

    def wyslij_rodo(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = formataddr(
            (str(Header(konsultant.kto, 'utf-8')), konsultant.login))
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
