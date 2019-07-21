import tkinter as tk
import sys
from server import Server
from pracownik import nowy_pracownik


class Window():
    def __init__(self, title, size):
        self.title = title
        self.size = size

        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.size)

        """Ustawienie na środku ekranu oraz ikonka."""
        self.root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.create_frames()

        self.root.mainloop()  # główny loop

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
