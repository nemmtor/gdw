from window import Window
import tkinter as tk
from config import konsultant, font10, font10b, entry_width


class Umowa(Window):
    '''frame = entry frame'''




    def widgets(self):
        page_frame = tk.Frame(self.root)

        left_frame = tk.Frame(page_frame)
        #mid_frame = tk.Frame(page_frame, bg='green')
        right_frame = tk.Frame(page_frame)
        menu_frame = tk.Frame(page_frame)
        left_frame.pack(fill=tk.BOTH, expand=False, side=tk.LEFT)
        #mid_frame.pack(fill=tk.BOTH, expan=True, side=tk.LEFT)
        right_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        menu_frame.pack(fill=tk.BOTH, expand=True)

        ##### MENU FRAME (po prawej stronie)
        zalog_label = tk.Label(menu_frame, text='Zalogowany jako:')
        zalog_label.pack(pady=10)
        # kons_label = tk.Label(page_frame, text=konsultant.kto,
        #                         font=('Arial 800', 10), fg='green')
        kons_label = tk.Label(menu_frame, text='Kacper Witas',
                                font=font10, fg='green')
        kons_label.pack()

        menu_button = tk.Button(menu_frame, text="MENU",
                            font=font10, width=10,
                            command=lambda: self.menu_butt())
        menu_button.pack(pady=20)

        dod_adresy_button = tk.Button(menu_frame, text="Dodaj odbiorce",
                                  font=font10, width=10,
                                  command=lambda: self.dod_butt())
        dod_adresy_button.pack()

        ##### MID FRAME
        img = tk.PhotoImage(file="pliki/goldwin.png")
        img_Label = tk.Label(right_frame, image=img)
        img_Label.image = img
        img_Label.place(relx=.5, rely=.5, anchor="c")

        ##### LEFT FRAME

        # Imie i nazwisko
        imie = tk.Label(left_frame, text="Imię i nazwisko:", font=font10b)
        imie.grid(row=0, column=0)
        imie_entry = tk.Entry(left_frame, width=entry_width)
        imie_entry.grid(row=0, column=1, sticky='E')

        # Numer telefonu
        tel = tk.Label(left_frame, text="Numer telefonu:", font=font10b)
        tel.grid(row=10, column=0)
        tel_entry = tk.Entry(left_frame, width=entry_width)
        tel_entry.grid(row=10, column=1)

        # Data sprzedaży
        sprz = tk.Label(left_frame, text="Data sprzedaży:", font=font10b)
        sprz.grid(row=20, column=0)
        sprz_entry = tk.Entry(left_frame, width=entry_width)
        sprz_entry.grid(row=20, column=1)

        # Date dostarczenia
        dost = tk.Label(left_frame, text="Data dostarczenia:", font=font10b)
        dost.grid(row=30, column=0)
        dost_entry = tk.Entry(left_frame, width=entry_width)
        dost_entry.grid(row=30, column=1)

        # Cena
        cena = tk.Label(left_frame, text="Cena/długość zobowiązania:", font=font10b)
        cena.grid(row=40, column=0)
        cena_entry = tk.Entry(left_frame, width=entry_width)
        cena_entry.grid(row=40, column=1)

        # Adres mailowy
        mail = tk.Label(left_frame, text="Adres mailowy", font=font10b)
        mail.grid(row=50, column=0)
        mail_entry = tk.Entry(left_frame, width=entry_width)
        mail_entry.grid(row=50, column=1)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=60, column=0)

        # Adres rejestrowy
        adr_rej = tk.Label(left_frame, text="Adres rejestrowy", font=font10b)
        adr_rej.grid(row=70, column=0)
        adr_rej_entry = tk.Entry(left_frame, width=entry_width)
        adr_rej_entry.grid(row=70, column=1)
        # Checkbox
        adr_rej_var = tk.IntVar(value=1)
        adr_rej_cb = tk.Checkbutton(left_frame, variable=adr_rej_var,
                                command=lambda: ukryj(adr_rej_entry, adr_rej_var))
        adr_rej_cb.select()
        adr_rej_cb.grid(row=70, column=2)

        # Adres adr_korespondencyjny
        adr_kor = tk.Label(left_frame, text="Adres korespondencyjny", font=font10b)
        adr_kor.grid(row=80, column=0)
        adr_kor_entry = tk.Entry(left_frame, width=entry_width)
        adr_kor_entry.grid(row=80, column=1)
        # Checkbox
        adr_kor_var = tk.IntVar(value=1)
        adr_kor_cb = tk.Checkbutton(left_frame, variable=adr_kor_var,
                                command=lambda: ukryj(adr_kor_entry, adr_kor_var))
        adr_kor_cb.select()
        adr_kor_cb.grid(row=80, column=2)

        # Adres dostarczenia
        adr_dost = tk.Label(left_frame, text="Adres dostarczenia", font=font10b)
        adr_dost.grid(row=90, column=0)
        adr_dost_entry = tk.Entry(left_frame, width=entry_width)
        adr_dost_entry.grid(row=90, column=1)
        # Checkbox
        adr_dost_var = tk.IntVar(value=1)
        adr_dost_cb = tk.Checkbutton(left_frame, variable=adr_dost_var,
                                command=lambda: ukryj(adr_dost_entry, adr_dost_var))
        adr_dost_cb.select()
        adr_dost_cb.grid(row=90, column=2)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=100, column=0)
        page_frame.pack(fill=tk.BOTH, expand=True)

        # Branża
        branza = tk.Label(left_frame, text="Branża:", font=font10b)
        branza.grid(row=110, column=0)
        branza_entry = tk.Entry(left_frame, width=entry_width)
        branza_entry.grid(row=110, column=1)

        # Pytania do prawnika
        pytania = tk.Label(left_frame, text="Pytania do prawnika:", font=font10b)
        pytania.grid(row=110, column=0)
        pytania_entry = tk.Entry(left_frame, width=entry_width)
        pytania_entry.grid(row=110, column=1)

        # Dodatkowe informacje
        dodatkowe = tk.Label(left_frame, text="Dodatkowe informacje:", font=font10b)
        dodatkowe.grid(row=120, column=0)
        dodatkowe_entry = tk.Entry(left_frame, width=entry_width)
        dodatkowe_entry.grid(row=120, column=1)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=130, column=0)

        # Załącznik
        zalacznik = tk.Button(left_frame, text="Załącznik", font=font10b)
        zalacznik.grid(row=140, column=0)

        # Wyślij
        wyslij = tk.Button(left_frame, text="Wyślij", font=font10b)
        wyslij.grid(row=140, column=1)

        page_frame.pack(fill=tk.BOTH, expand=True)

new = Umowa('Umowa', '800x300')
