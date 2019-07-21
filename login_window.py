from window import Window
import tkinter as tk
from server import Server
from pracownik import nowy_pracownik


class LoginWindow(Window):

    def press_login(self, login_entry, password_entry):
        login = login_entry.get()
        password = password_entry.get()
        polacz = Server()
        if polacz.sprawdz_haslo(login, password):
            nowy_pracownik.login = login
            nowy_pracownik.password = password
            self.root.destroy()
            return

    def create_frames(self):
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

        submit = tk.Button(page_frame, text="Zaloguj",
                           command=lambda: self.press_login(
                               login_entry,
                               password_entry))
        submit.pack()