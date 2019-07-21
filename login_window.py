from window import Window
import tkinter as tk
from tkinter import messagebox
from server import Server
from pracownik import konsultant


class LoginWindow(Window):
    '''Klasa inherituje z Window.
    Tworzy okienko logowania.'''

    def press_login(self, login_entry, password_entry):
        '''Funkcja przycisku /Zaloguj/'''
        login = login_entry.get()
        password = password_entry.get()
        polacz = Server()  # Tworzy połączenie smtp
        if polacz.sprawdz_haslo(login, password):
            #  Jeżeli dane są prawidłowe to
            konsultant.login = login
            konsultant.password = password
            konsultant.dane(login, password)
            messagebox.showinfo(
                'Ok', 'Zalogowano jako {}'.format(konsultant.kto))
            self.root.destroy()  # Usuwa okienko logowania
            return
        else:
            messagebox.showinfo('Error', 'Błędny login.')
            login_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

    def widgets(self):
        page_frame = tk.Frame(self.root)
        login_label = tk.Label(page_frame, text='Login:')
        login_label.pack()
        login_entry = tk.Entry(page_frame)
        login_entry.pack()

        password_label = tk.Label(page_frame, text='Hasło:')
        password_label.pack()
        password_entry = tk.Entry(page_frame, show='*')
        password_entry.pack()
        page_frame.pack()

        submit = tk.Button(page_frame, text='Zaloguj',
                           command=lambda: self.press_login(
                               login_entry,
                               password_entry))
        submit.pack()
        return
