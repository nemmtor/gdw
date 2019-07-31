'''Okno logowania.'''
from config import entry_width  # konfiguracja
from window import Window  # klasa okna
from tkinter import messagebox  # popup message
from server import server  # sprawdzenie czy jest połączenie (login/pw)
import tkinter as tk
# Obiekty
from konsultant import konsultant


class Login(Window):
    '''Tworzy okienko logowania. Inherituje z Window.'''

    def press_login(self):
        '''Funkcja przycisku Zaloguj'''
        # Pobranie danych z entry
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Sprawdzenie czy dane są prawidłowe
        if server.sprawdz_haslo(login, password):
            # Wysyła dane z entry do obiektu
            konsultant.dane(login, password)

            # Popup
            messagebox.showinfo(
                'Zalogowano', 'Zalogowano jako {}'.format(konsultant.kto))

            # Usunięcie okienka logowania
            self.root.destroy()
        else:
            # Popup
            messagebox.showinfo('Error', 'Błędny login.')

            # Wyczyszczenie Entry
            self.login_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

    def widgets(self):
        '''Widgety okna.'''
        # Główny frame
        page_frame = tk.Frame(self.root)

        # Login label, entry
        login_label = tk.Label(page_frame, text='Login:')
        self.login_entry = tk.Entry(page_frame, width=entry_width)

        # Password label, entry
        password_label = tk.Label(page_frame, text='Hasło:')
        self.password_entry = tk.Entry(page_frame, width=entry_width, show='*')

        # Przycisk zaloguj
        submit = tk.Button(page_frame, text='Zaloguj',
                           command=lambda: self.press_login())

        #Pack
        login_label.pack()
        self.login_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        page_frame.pack()
        submit.pack()
