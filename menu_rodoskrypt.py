'''Okno menu. Aneks i wypowiedzenie do zrobienia później.'''
from window import Window  # klasa okna
import tkinter as tk
from config import font10, entry_width, brwid

# Obiekty
from konsultant import konsultant
from mailsender import mailsender


class Rodo_Skrypt(Window):

    def widgets(self):
        '''Widgety'''

        # Główny frame
        page_frame = tk.Frame(self.root)
        zalog_frame = tk.Frame(page_frame)
        mail_frame = tk.Frame(page_frame)
        buttons_frame = tk.Frame(page_frame)

        # Informacja kto zalogowany
        # Label
        zalog_label = tk.Label(zalog_frame, text='Zalogowano jako:')
        # Label z imieniem i nazwiskiem
        kons_label = tk.Label(zalog_frame, text=konsultant.kto,
                              font=font10, fg='green')
        # Entry
        # Mail klienta
        mail_label = tk.Label(mail_frame, text='Mail klienta', font=font10)
        mail_entry = tk.Entry(mail_frame, width=entry_width, borderwidth=brwid)
        mail_entry.bind_class(
            "Entry", "<Button-3><ButtonRelease-3>", self.show_menu)

        # Przyciski
        menu_butt = tk.Button(buttons_frame, text='MENU', font=font10,
                              width=10, command=lambda: self.menu_butt())
        wyslij_butt = tk.Button(buttons_frame, text='WYŚLIJ', font=font10,
                                width=10,
                                command=lambda:
                                mailsender.rodo_inf(mail_entry.get().strip(),
                                                    self.root))

        # Pack

        zalog_label.pack()
        kons_label.pack()

        mail_label.pack()
        mail_entry.pack()

        menu_butt.pack(side=tk.LEFT)
        wyslij_butt.pack(pady=10, padx=20)

        zalog_frame.grid(row=1, column=1, columnspan=2)
        mail_frame.grid(row=2, column=1, columnspan=2)
        # separator.grid(row=4)
        buttons_frame.grid(row=3, column=1, columnspan=2)

        page_frame.pack()
