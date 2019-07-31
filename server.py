# -*- coding: utf-8 -*-
'''Sprawdzenie czy login/hasło są prawidłowe.
Połączenie smtp z szyfrowaniem tls.'''
import smtplib
import imaplib
import os
import time
from config import konsultant, mailsender, klient
from tresc_maila import stworz_body, stworz_subject, stworz_rodo
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from tkinter import messagebox  # popup message


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
            self.quit()
            return True
        except (smtplib.SMTPAuthenticationError,
                TypeError):
            return False

    def wyslij_rodo(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        for adres in mailsender.dod_odbiorcy:
            if adres != '':
                mailsender.odbiorcy.append(adres)
        msg['To'] = klient.mail

        msg['Subject'] = 'Grupa Prawna Goldwin'
        msg['Date'] = formatdate(localtime=True)
        msg['Bcc'] = 'administrator@bedekoderem.pl'
        msg.attach(MIMEText(stworz_rodo(), 'html'))
        self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
        self.smtp.starttls()
        self.smtp.login(self.login, self.password)
        self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')
        self.imap.starttls()
        self.imap.login(self.login, self.password)
        self.smtp.send_message(msg)
        self.imap.append('SENT', '\\Seen',
                         imaplib.Time2Internaldate(time.time()),
                         msg.as_string().encode('utf8'))


    def wyslij_maila(self):
        msg = MIMEMultipart('mixed')
        msg['From'] = konsultant.login
        for adres in mailsender.dod_odbiorcy:
            if adres != '':
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
            self.smtp = smtplib.SMTP('smtp.gpgoldwin.pl:587')
            self.smtp.starttls()
            self.smtp.login(self.login, self.password)
            self.imap = imaplib.IMAP4('imap.gpgoldwin.pl')
            self.imap.starttls()
            self.imap.login(self.login, self.password)
            self.smtp.send_message(msg)
            self.imap.append('SENT', '\\Seen',
                             imaplib.Time2Internaldate(time.time()),
                             msg.as_string().encode('utf8'))
            return True
        except AttributeError:
            messagebox.showinfo('Error', 'Nie dodałeś załącznika.')

    def dodaj_maila():
        pass

    def quit(self):
        '''Kończy sesje.'''
        self.smtp.quit()


server = Server()
