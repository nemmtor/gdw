'''Okno logowania, sprawdza czy login/hasło są prawidłowe.
Jeżeli tak to przepuszcza dalej.'''
from config import konsultant, entry_width  # konfiguracja
from window import Window  # klasa okna
from tkinter import messagebox  # popup message
from server import Server  # sprawdzenie czy jest połączenie (login/pw)
import tkinter as tk

class Login(Window):
    '''Tworzy okienko logowania.'''

    def press_login(self, login_entry, password_entry):
        '''Funkcja przycisku /Zaloguj/'''
        login = login_entry.get()  # pobiera login z entry
        password = password_entry.get()  # pobiera haslo z entry
        polacz = Server()  # Tworzy połączenie smtp + tls
        if polacz.sprawdz_haslo(login, password):
            #  Jeżeli dane są prawidłowe to
            #  zapisuje maila i hasło w obiekcie konsultant
            konsultant.login = login
            konsultant.password = password
            konsultant.dane(login, password)
            # popup
            messagebox.showinfo(
                'Ok', 'Zalogowano jako {}'.format(konsultant.kto))
            self.root.destroy()  # Usuwa okienko logowania
        else:
            #popup
            messagebox.showinfo('Error', 'Błędny login.')
            login_entry.delete(0, tk.END)  # czyści entry
            password_entry.delete(0, tk.END)  # czyści entry

    def widgets(self):
        '''Widgety, zmienić na self?'''
        page_frame = tk.Frame(self.root)  # główny frame
        login_label = tk.Label(page_frame, text='Login:')
        login_label.pack()
        login_entry = tk.Entry(page_frame, width=entry_width)
        login_entry.pack()

        password_label = tk.Label(page_frame, text='Hasło:')
        password_label.pack()
        password_entry = tk.Entry(page_frame, width=entry_width, show='*')
        password_entry.pack()
        page_frame.pack()

        # Submit wysyła dane z entry do funkcji press login
        submit = tk.Button(page_frame, text='Zaloguj',
                           command=lambda: self.press_login(
                               login_entry,
                               password_entry))
        submit.pack()
