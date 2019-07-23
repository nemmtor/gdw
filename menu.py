from window import Window
import tkinter as tk
from config import konsultant  # dane konsultanta


def umowa_button(root):
    konsultant.menu(1)
    root.destroy()


def aneks_button(root):
    konsultant.menu(2)
    root.destroy()


def sprawy_button(root):
    konsultant.menu(3)
    root.destroy()


def wypo_button(root):
    konsultant.menu(4)
    root.destroy()


class Menu(Window):

    def widgets(self):
        page_frame = tk.Frame(self.root)

        #  Informacja kto zalogowany
        zalog_label = tk.Label(page_frame, text='Zalogowany jako:')
        zalog_label.pack()
        kons_label = tk.Label(page_frame, text=konsultant.kto,
                                font=('Arial 800', 10), fg='green')
        kons_label.pack()

        # Przycisk umowa
        umowa = tk.Button(page_frame, text='Umowa', font=('Arial Bold', 12),
                      height=2, width=18,
                      command=lambda: umowa_button(self.root))
        umowa.pack()

        # Przycisk sprawy nierozwiązane
        sprawy = tk.Button(page_frame, text='Sprawy nierozwiązane',
                       font=('Arial Bold', 12), height=2, width=18,
                       command=lambda: sprawy_button(self.root))
        sprawy.pack()

        # Przycisk aneks
        aneks = tk.Button(page_frame, text='Aneks', font=('Arial Bold', 12),
                      height=2, width=18,
                      command=lambda: aneks_button(self.root))
        aneks.pack()

        # Przycisk wypowiedzenie
        wypo = tk.Button(page_frame, text='Wypowiedzenie', font=('Arial Bold', 12),
                     height=2, width=18,
                     command=lambda: wypo_button(self.root))
        wypo.pack()


        page_frame.pack()
