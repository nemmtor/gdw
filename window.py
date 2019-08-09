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
        self.make_menu()


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

    def make_menu(self):
        self.the_menu = tk.Menu(self.root, tearoff=0)
        self.the_menu.add_command(label="Wytnij")
        self.the_menu.add_command(label="Kopiuj")
        self.the_menu.add_command(label="Wklej")

    def show_menu(self, e):
        w = e.widget
        self.the_menu.entryconfigure("Wytnij",
        command=lambda: w.event_generate("<<Cut>>"))
        self.the_menu.entryconfigure("Kopiuj",
        command=lambda: w.event_generate("<<Copy>>"))
        self.the_menu.entryconfigure("Wklej",
        command=lambda: w.event_generate("<<Paste>>"))
        self.the_menu.tk.call("tk_popup", self.the_menu, e.x_root, e.y_root)

    def ukryj(self, entry, var):
        '''Funkcja blokowania entry adresów.'''
        if var.get():
            entry.config(state='disabled')
        else:
            entry.config(state='normal')

    def menu_butt(self):
        self.root.destroy()

    def wyslij_butt(self):
        klient.stworz_klienta(self.imie_entry.get().strip(),
                              self.tel_entry.get().strip(),
                              self.sprz_entry.get().strip(),
                              self.dost_entry.get().strip(),
                              self.cena_entry.get().strip(),
                              self.mail_entry.get().strip(),
                              self.branza_entry.get().strip(),
                              self.pytania_entry.get().strip(),
                              self.dodatkowe_entry.get("1.0", tk.END).strip(),
                              self.adr_rej_var.get(),
                              self.adr_kor_var.get(),
                              self.adr_dost_var.get(),
                              self.adr_rej_entry.get().strip(),
                              self.adr_kor_entry.get().strip(),
                              self.adr_dost_entry.get().strip(),
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
                    self.root.destroy()
            except smtplib.SMTPRecipientsRefused:
                messagebox.showinfo('Error',
                                    'Niepoprawny adres mailowy.')
