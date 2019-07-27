# -*- coding: utf-8 -*-
'''Sprawdzenie czy login/hasło są prawidłowe.
Połączenie smtp z szyfrowaniem tls.'''
import smtplib
import imaplib
import os
import time
from config import konsultant, mailsender
from tresc_maila import stworz_body, stworz_subject
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


class Server():
    def __init__(self):
        '''Tworzy połaczenie smtp.'''
        self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        self.smtp.starttls()
        self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')
        self.imap.starttls()

    def sprawdz_haslo(self, login, password):
        '''Sprawdza czy login/hasło są prawidłowe.'''
        self.login = login
        self.password = password
        try:
            self.smtp.login(self.login, self.password)
            self.imap.login(self.login, self.password)
            return True
        except (smtplib.SMTPAuthenticationError,
                TypeError):
            return False

    def wyslij_maila(self):
        msg = MIMEMultipart()
        msg['From'] = konsultant.login
        for adres in mailsender.dod_odbiorcy:
            if adres != '':
                mailsender.odbiorcy.append(adres)
        msg['To'] = ', '.join(mailsender.odbiorcy)

        msg['Subject'] = stworz_subject()
        msg["Date"] = formatdate(localtime=True)

        msg.attach(MIMEText(stworz_body(), 'html'))

        attachment = open(mailsender.zalacznik, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= " +
                        os.path.basename(mailsender.zalacznik))

        msg.attach(part)
        self.smtp.send_message(msg)
        self.imap.append('SENT', '\\Seen',
                         imaplib.Time2Internaldate(time.time()),
                         msg.as_string().encode('utf8'))

    def dodaj_maila():
        pass

    def quit(self):
        '''Kończy sesje.'''
        self.smtp.quit()


server = Server()
