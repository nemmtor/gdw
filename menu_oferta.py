'''Okno menu. Aneks i wypowiedzenie do zrobienia później.'''
from window import Window  # klasa okna
import tkinter as tk
from config import font10, entry_width

# Obiekty
from konsultant import konsultant

class Menu_Oferta(Window):

    # Funkcje przycisków:
    def plec_butt(self, wybor):
        '''Wybór menu, następnie usunięcie okna menu.'''
        konsultant.menu(wybor)
        self.root.destroy()

    def widgets(self):
        '''Widgety'''

        # Główny frame
        page_frame = tk.Frame(self.root)
        zalog_frame = tk.Frame(page_frame)
        plec_frame = tk.Frame(page_frame)
        cena_frame = tk.Frame(page_frame)
        mail_frame = tk.Frame(page_frame)

        # Informacja kto zalogowany
        # Label
        zalog_label = tk.Label(zalog_frame, text='Zalogowany jako:')
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
                          # Pani
        pani = tk.Radiobutton(plec_frame, text='Pani', font=font10,
                              variable=self.plec, value=2)

        cena129 = tk.Radiobutton(cena_frame, text='129zł', font=font10,
                                    variable=self.cena, value=129)

        cena159 = tk.Radiobutton(cena_frame, text='159zł', font=font10,
                                    variable=self.cena, value=159)

        cena199 = tk.Radiobutton(cena_frame, text='199zł', font=font10,
                                    variable=self.cena, value=199)

        # Entry
        # Mail klienta
        mail_label = tk.Label(mail_frame, text='Mail klienta', font=font10)
        mail_entry = tk.Entry(mail_frame, width=entry_width)

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

        zalog_frame.grid(row=1, column=1)
        plec_frame.grid(row=2, column=1)
        cena_frame.grid(row=2, column=2)
        mail_frame.grid(row=3, column=1, columnspan=2)

        page_frame.pack()
