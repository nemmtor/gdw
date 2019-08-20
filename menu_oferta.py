'''Okno menu. Aneks i wypowiedzenie do zrobienia później.'''
from window import Window  # klasa okna
import tkinter as tk
from config import font9, font10, entry_width, brwid

# Obiekty
from konsultant import konsultant
from mailsender import mailsender


class Menu_Oferta(Window):

    def widgets(self):
        '''Widgety'''

        # Główny frame
        page_frame = tk.Frame(self.root)
        zalog_frame = tk.Frame(page_frame)
        plec_frame = tk.Frame(page_frame)
        cena_frame = tk.Frame(page_frame)
        mail_frame = tk.Frame(page_frame)
        buttons_frame = tk.Frame(page_frame)

        # Informacja kto zalogowany
        # Label
        zalog_label = tk.Label(zalog_frame, text='Zalogowano jako:')
        # Label z imieniem i nazwiskiem
        kons_label = tk.Label(zalog_frame, text=konsultant.kto,
                              font=font10, fg='green')
        # Label - zwrot grzecznościowy
        zwrot_label = tk.Label(plec_frame, text='Zwrot\ngrzecznościowy',
                               font=font10)
        cena_label = tk.Label(cena_frame, text='Cena\npakietu',
                              font=font10)

        # Płeć
        self.plec = tk.IntVar()
        self.cena = tk.IntVar()
        # Pan
        pan = tk.Radiobutton(plec_frame, text='Pan', font=font10,
                             variable=self.plec, value=1)
        pan.select()
        # Pani
        pani = tk.Radiobutton(plec_frame, text='Pani', font=font10,
                              variable=self.plec, value=2)

        cena129 = tk.Radiobutton(cena_frame, text='129zł', font=font10,
                                 variable=self.cena, value=129)

        cena129.select()

        cena159 = tk.Radiobutton(cena_frame, text='159zł', font=font10,
                                 variable=self.cena, value=159)

        cena199 = tk.Radiobutton(cena_frame, text='199zł', font=font10,
                                 variable=self.cena, value=199)

        # Entry
        # Mail klienta
        mail_label = tk.Label(mail_frame, text='Mail klienta', font=font10)
        mail_entry = tk.Entry(mail_frame, width=entry_width, borderwidth=brwid, font=font9)
        mail_entry.bind_class(
            "Entry", "<Button-3><ButtonRelease-3>", self.show_menu)

        # Przyciski
        menu_butt = tk.Button(buttons_frame, text='MENU', font=font10,
                              width=12, padx=10, command=lambda: self.menu_butt())
        wyslij_butt = tk.Button(buttons_frame, text='WYŚLIJ', font=font10,
                                width=12, padx=10,
                                command=lambda:
                                mailsender.oferta(self.cena.get(),
                                                  self.plec.get(),
                                                  mail_entry.get().strip(),
                                                  self.root))

        # Pack

        zalog_label.pack()
        kons_label.pack()

        zwrot_label.pack()
        pan.pack()
        pani.pack()

        cena_label.pack()
        cena129.pack()
        cena159.pack()
        cena199.pack()

        mail_label.pack()
        mail_entry.pack()

        menu_butt.pack(side=tk.LEFT, pady=10, padx=(10, 10))
        wyslij_butt.pack(pady=10, padx=(10,10))

        zalog_frame.grid(row=1, column=1, columnspan=2)
        plec_frame.grid(row=2, column=1)
        cena_frame.grid(row=2, column=2)
        mail_frame.grid(row=3, column=1, columnspan=2)
        # separator.grid(row=4)
        buttons_frame.grid(row=5, column=1, columnspan=2)

        page_frame.pack()

if __name__ == '__main__':
    konsultant.kto = 'Developer ON'
    menu_oferta = Menu_Oferta('Goldwin Mailsender')
