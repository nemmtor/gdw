'''Okno logowania.'''
# from config import entry_width  # konfiguracja
import re  # regex dla sprawdzenia maila
from window import Window  # klasa okna
from tkinter import messagebox  # popup message
from server import server  # sprawdzenie czy jest połączenie (login/pw)
import tkinter as tk
# Obiekty
from konsultant import konsultant
from config import brwid, font9, font12, font12b

# Regex
# Sprawdza czy mail ma domene gpgoldwin.pl
mail_expr_goldwin = re.compile(r'^(.+?)@gpgoldwin.pl')


class Login(Window):
    '''Tworzy okienko logowania. Inherituje z Window.'''

    def press_login(self, value):
        '''Funkcja przycisku Zaloguj'''
        # Sprawdź czy mail ma poprawną formułę(domena gpgoldwin.pl)
        if re.match(mail_expr_goldwin, self.login_entry.get().strip()):
            konsultant.dane(self.login_entry.get().strip(),
                            self.password_entry.get().strip())
            # Sprawdzenie czy login/pw są prawidłowe
            if server.zaloguj():
                # Pokaż popup, że zalogowano
                messagebox.showinfo(
                    'Zalogowano', 'Zalogowano jako {}'.format(konsultant.kto))
                '''Test'''
                server.rozlacz()
                # Usunięcie okienka logowania
                self.root.destroy()
            else:
                # Popup
                messagebox.showinfo('Error', 'Błędny login.')
                # Wyczyszczenie Entry
                self.login_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
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
        login_label = tk.Label(page_frame, text='Login:', font=font12b)
        self.login_entry = tk.Entry(
            page_frame, width=30, borderwidth=brwid, font=font9)
        self.login_entry.bind_class(
            "Entry", "<Button-3><ButtonRelease-3>", self.show_menu)

        # Password label, entry
        password_label = tk.Label(page_frame, text='Hasło:', font=font12b)
        self.password_entry = tk.Entry(
            page_frame, width=30, show='*', borderwidth=brwid, font=font9)

        # Przycisk zaloguj
        submit = tk.Button(page_frame, text='Zaloguj', width=10,
                           padx=10, font=font12,
                           command=lambda: self.press_login(None))

        self.root.bind('<Return>', self.press_login)

        # Pack
        login_label.pack()
        self.login_entry.pack()
        password_label.pack(pady=(10, 0))
        self.password_entry.pack()
        submit.pack(pady=(10, 0))
        page_frame.pack(padx=30, pady=(5, 15))


if __name__ == '__main__':
    login = Login('Goldwin Mailsender')
