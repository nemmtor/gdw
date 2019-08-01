'''Główna klasa window, z której inne inheritują.
Tutaj ustawia się: tytuł, rozmiar, umieszczenie okna na środku ekranu.
Funkcja create frames jest pusta, klasa która inherituje musi nadpisać
funkcję createframes, tam ustawia się widgety.'''

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox  # popup message
import sys
import os
from config import entry_width, font10
from klient import klient
from mailsender import mailsender
from server import server
from bezpolskich import stworz_plik_ascii
import smtplib


class Window():
    def __init__(self, title, size):
        '''Ustawienie tytułu, rozmiaru'''
        self.title = title
        self.size = size
        self.filename = ''

        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.size)

        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.widgets()  # widgety

        self.root.mainloop()  # główny loop

    def widgets(self):
        pass

    def dod_butt(self):
        self.top = tk.Toplevel()
        self.top.title("Dodaj odbiorców")
        self.top.geometry('250x150')
        self.top.tk.call('wm', 'iconphoto',
                         self.top._w, tk.PhotoImage(file='pliki/ikona.gif'))

        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.top.protocol('WM_DELETE_WINDOW', lambda: self.wez_adresy())
        self.top.tk.call('wm', 'iconphoto', self.top._w,
                         tk.PhotoImage(file='pliki/ikona.gif'))
        self.top.update_idletasks()
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        x = (self.top.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top.winfo_screenheight() // 2) - (height // 2)
        self.top.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Dodatkowe adresy
        adresy_frame = tk.Frame(self.top)
        adresy_frame.pack()

        self.adres1 = tk.Entry(adresy_frame, width=entry_width)
        self.adres1.pack(pady=5)
        self.adres1.insert(tk.END, mailsender.dod_odbiorcy[0])

        self.adres2 = tk.Entry(adresy_frame, width=entry_width)
        self.adres2.pack(pady=5)
        self.adres2.insert(tk.END, mailsender.dod_odbiorcy[1])

        self.adres3 = tk.Entry(adresy_frame, width=entry_width)
        self.adres3.pack(pady=5)
        self.adres3.insert(tk.END, mailsender.dod_odbiorcy[2])

        ok_butt = tk.Button(self.top, text="Zapisz",
                            font=font10, width=10,
                            command=lambda: self.wez_adresy())
        ok_butt.pack()

    def ukryj(self, entry, var):
        '''Funkcja blokowania entry adresów.'''
        if var.get():
            entry.config(state='disabled')
        else:
            entry.config(state='normal')

    def wez_adresy(self):
        '''Pobiera adresy z entry'''
        dodatkowi = [self.adres1.get(), self.adres2.get(), self.adres3.get()]
        mailsender.dodatkowi(dodatkowi)
        self.top.destroy()

    def menu_butt(self):
        self.root.destroy()

    def zal_butt(self):
        '''Dodawanie załącznika.'''
        mailsender.plik(askopenfilename())
        if mailsender.zalacznik != '':
            mailsender.zalacznik = stworz_plik_ascii(mailsender.zalacznik)
            self.zal_label.configure(text=mailsender.zalacznik, fg='green')

    def wyslij_butt(self):
        klient.stworz_klienta(self.imie_entry.get(),
                              self.tel_entry.get(),
                              self.sprz_entry.get(),
                              self.dost_entry.get(),
                              self.cena_entry.get(),
                              self.mail_entry.get(),
                              self.branza_entry.get(),
                              self.pytania_entry.get(),
                              self.dodatkowe_entry.get(),
                              self.adr_rej_var.get(),
                              self.adr_kor_var.get(),
                              self.adr_dost_var.get(),
                              self.adr_rej_entry.get(),
                              self.adr_kor_entry.get(),
                              self.adr_dost_entry.get()
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
                mailsender.wyslij_rodo()
                if mailsender.wyslij_sprzedazowy():
                    klient.rej = ''
                    klient.kor = ''
                    klient.dost = ''
                    messagebox.showinfo('Wysłano',
                    'Wysłano maila sprzedażowego oraz maila z RODO.')
                    os.remove(mailsender.zalacznik)
                    self.root.destroy()
            except smtplib.SMTPRecipientsRefused:
                messagebox.showinfo('Error',
                'Niepoprawny adres mailowy.')
