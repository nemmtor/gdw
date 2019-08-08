'''Główna klasa window, z której inne inheritują.
Tutaj ustawia się: tytuł, rozmiar, umieszczenie okna na środku ekranu.
Funkcja create frames jest pusta, klasa która inherituje musi nadpisać
funkcję createframes, tam ustawia się widgety.'''

import tkinter as tk
from tkinter import messagebox  # popup message
import sys
import os
# from config import entry_width, font10
from klient import klient
from konsultant import konsultant
from mailsender import mailsender
import smtplib
from server import server
from config import ikona


class Window():
    # usunalem size z nawiasow
    def __init__(self, title):
        '''Ustawienie tytułu, rozmiaru'''
        self.title = title
        # self.size = size
        self.filename = ''

        self.root = tk.Tk()
        self.root.title(self.title)


        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file=ikona))
        self.widgets()
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2)  - (width // 2)
        y = (self.root.winfo_screenheight() // 2)  - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        # self.root.geometry('{}x{}'.format(width, height))

        # self.widgets()  # widgety

        self.root.mainloop()  # główny loop

    def ukryj(self, entry, var):
        '''Funkcja blokowania entry adresów.'''
        if var.get():
            entry.config(state='disabled')
        else:
            entry.config(state='normal')

    def menu_butt(self):
        self.root.destroy()

    def wyslij_butt(self):
        klient.stworz_klienta(self.imie_entry.get(),
                              self.tel_entry.get(),
                              self.sprz_entry.get(),
                              self.dost_entry.get(),
                              self.cena_entry.get(),
                              self.mail_entry.get(),
                              self.branza_entry.get(),
                              self.pytania_entry.get(),
                              self.dodatkowe_entry.get("1.0", tk.END),
                              self.adr_rej_var.get(),
                              self.adr_kor_var.get(),
                              self.adr_dost_var.get(),
                              self.adr_rej_entry.get(),
                              self.adr_kor_entry.get(),
                              self.adr_dost_entry.get(),
                              self.spr_nierozw_var.get()
                              )
        error = False
        if klient.imnaz == '':
            messagebox.showinfo('Error', 'Brak imienia i nazwiska')
            error = True
        if klient.tel == '':
            messagebox.showinfo('Error', 'Brak numeru telefonu')
            error = True
        if klient.datasprz == '':
            messagebox.showinfo('Error', 'Brak daty sprzedaży')
            error = True
        if klient.datawys == '':
            messagebox.showinfo('Error', 'Brak daty doręczenia')
            error = True
        if klient.cena_dl == '':
            messagebox.showinfo('Error', 'Brak ceny/dł. zobowiązania')
            error = True
        if klient.mail == '':
            messagebox.showinfo('Error', 'Brak adresu mailowego')
            error = True
        if klient.branza == '':
            messagebox.showinfo('Error', 'Brak branży')
            error = True
        if klient.pytania == '':
            messagebox.showinfo('Error', 'Brak pytań do prawnika')
            error = True
        if klient.dodatkowe == '':
            messagebox.showinfo('Error', 'Brak dodatkowych informacji')
            error = True
        if not error:
            try:
                if konsultant.wybor == 1:
                    server.zaloguj()
                    mailsender.wyslij_rodo()
                if mailsender.wyslij_sprzedazowy():
                    klient.rej = ''
                    klient.kor = ''
                    klient.dost = ''
                    messagebox.showinfo(
                        'Wysłano',
                        'Wysłano maila sprzedażowego oraz maila z RODO.')
                    server.rozlacz()
                    os.remove(mailsender.zalacznik)
                    self.root.destroy()
            except smtplib.SMTPRecipientsRefused:
                messagebox.showinfo('Error',
                                    'Niepoprawny adres mailowy.')
