'''Okno umowy.'''
from window import Window
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
from config import entry_width, stworz_date, brwid, font20b
from config import font9, font10, font10b, img_resizer, goldwin
from PIL import ImageTk
from konsultant import konsultant
from mailsender import mailsender

# from config import goldwin


class Umowa(Window):
    '''frame = entry frame'''

    def dod_butt(self):
        self.top = tk.Toplevel()
        self.top.title('Dodatkowi odbiorcy')
        self.top.grab_set()
        # Dodatkowe adresy
        adresy_frame = tk.Frame(self.top)
        adresy_frame.pack()

        self.adres1 = tk.Entry(adresy_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.adres1.pack(pady=5)
        self.adres1.insert(tk.END, mailsender.dod_odbiorcy[0])

        self.adres2 = tk.Entry(adresy_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.adres2.pack(pady=5)
        self.adres2.insert(tk.END, mailsender.dod_odbiorcy[1])

        self.adres3 = tk.Entry(adresy_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.adres3.pack(pady=5)
        self.adres3.insert(tk.END, mailsender.dod_odbiorcy[2])

        ok_butt = tk.Button(self.top, text='Zapisz',
                            font=font10, width=15,
                            command=lambda: self.wez_adresy())
        ok_butt.pack()
        self.center(self.top, False)

    def wez_adresy(self):
        '''Pobiera adresy z entry'''
        mailsender.dod_odbiorcy = [
            self.adres1.get().strip(),
            self.adres2.get().strip(),
            self.adres3.get().strip()]
        self.top.destroy()

    def zmienvar(self):
        if self.spr_nierozw_var == 0:
            self.spr_nierozw_var == 1
        else:
            self.spr_nierozw_var == 0



    def zal_butt(self):
        '''Dodawanie załącznika.'''
        #  Musi być osobna zmienna, problem z cancel przy wybieraniu zalacznika
        zalacznik = askopenfilename()
        if zalacznik != '' and zalacznik != ():
            mailsender.zalacznik = zalacznik
            self.zal_label.configure(
                text=mailsender.zalacznik.split(r'/')[-1], fg='green')

    def ukryj(self, entry, var):
        '''Funkcja blokowania entry adresów.'''
        if self.rej_var.get() != 1 and\
                self.kor_var.get() != 1 and\
                self.dost_var.get() != 1:
            self.adr_1_entry.config(state='disabled')

        if self.rej_var.get() != 2 and\
                self.kor_var.get() != 2 and\
                self.dost_var.get() != 2:
            self.adr_2_entry.config(state='disabled')

        if self.rej_var.get() != 3 and\
                self.kor_var.get() != 3 and\
                self.dost_var.get() != 3:
            self.adr_3_entry.config(state='disabled')

        if entry is not None and var is not None:
            if var.get():
                entry.config(state='normal')
            else:
                entry.config(state='disabled')

    def widgets(self):
        '''Widgety.'''
        self.hidden = False
        page_frame = tk.Frame(self.root)

        left_frame = tk.Frame(page_frame)
        right_frame = tk.Frame(page_frame)
        # menu_frame = tk.Frame(page_frame)
        menu_frame = tk.Frame(page_frame)
        # W Menu frame
        rozne_frame = tk.Frame(menu_frame)



        # MENU FRAME (po prawej stronie)
        img = ImageTk.PhotoImage(img_resizer(goldwin, 0.45))
        img_Label = tk.Label(menu_frame, image=img)
        img_Label.image = img
        img_Label.pack()

        zalog_label = tk.Label(menu_frame, text='Zalogowano jako:')
        zalog_label.pack()
        kons_label = tk.Label(menu_frame, text=konsultant.kto,
                              font=font10, fg='green')
        kons_label.pack()

        menu_button = tk.Button(menu_frame, text='MENU',
                                font=font10, width=12, padx=10,
                                command=lambda: self.menu_butt())
        menu_button.pack(pady=(10, 0))

        dod_adresy_button = tk.Button(menu_frame, text='Dodaj odbiorce',
                                      font=font10, width=12, padx=10,
                                      command=lambda: self.dod_butt())
        dod_adresy_button.pack()

        # Sprawy nierozwiązane
        self.spr_nierozw_var = tk.IntVar(value=0)
        self.spr_nierozw_cb = tk.Checkbutton(rozne_frame,
                                             text='Sprawy\nnierozwiązane',
                                             variable=self.spr_nierozw_var,
                                             font=font10,
                                             command=lambda: self.zmienvar())
        self.spr_nierozw_cb.pack()


        # MID FRAME
        # img = tk.PhotoImage(file=goldwin)
        # img_Label = tk.Label(right_frame, image=img)
        # img_Label.image = img
        # img_Label.place(relx=.5, rely=.5, anchor='c')

        # LEFT FRAME

        # Imie i nazwisko
        imie = tk.Label(left_frame, text='Imię i nazwisko:', font=font10b)
        imie.grid(row=0, column=0)
        self.imie_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.imie_entry.grid(row=0, column=1)
        self.imie_entry.bind_class(
            'Entry', '<Button-3><ButtonRelease-3>', self.show_menu)

        # Numer telefonu
        tel = tk.Label(left_frame, text='Numer telefonu:', font=font10b)
        tel.grid(row=10, column=0)
        self.tel_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.tel_entry.grid(row=10, column=1)

        # Data sprzedaży
        sprz = tk.Label(left_frame, text='Data sprzedaży:', font=font10b)
        sprz.grid(row=20, column=0)
        self.sprz_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.sprz_entry.insert(0, stworz_date('dzis'))
        self.sprz_entry.grid(row=20, column=1)

        # Date dostarczenia
        dost = tk.Label(left_frame, text='Data dostarczenia:', font=font10b)
        dost.grid(row=30, column=0)
        self.dost_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.dost_entry.grid(row=30, column=1)

        # Cena
        cena = tk.Label(
            left_frame, text='Cena/długość:', font=font10b)
        cena.grid(row=40, column=0)
        self.cena_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.cena_entry.grid(row=40, column=1)

        # Adres mailowy
        mail = tk.Label(left_frame, text='Adres mailowy', font=font10b)
        mail.grid(row=50, column=0)
        self.mail_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.mail_entry.grid(row=50, column=1)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=60, column=0)

        # Adresy
        # Frame dla radiobuttonow
        adresy_frame = tk.Frame(left_frame)
        adresy_frame.grid(row=62, column=0, rowspan=5, columnspan=2)

        # rkd labele
        r_label = tk.Label(adresy_frame, text='rej', font=font10b)
        r_label.grid(row=0, column=1, pady=10)

        k_label = tk.Label(adresy_frame, text='kor', font=font10b)
        k_label.grid(row=0, column=2)

        d_label = tk.Label(adresy_frame, text='dost', font=font10b)
        d_label.grid(row=0, column=3)

        # vary
        self.rej_var = tk.IntVar(value=0)
        self.kor_var = tk.IntVar(value=0)
        self.dost_var = tk.IntVar(value=0)

        # RADIO BUTTONY
        # REJESTROWY

        # Ceidg REJESTROWY
        ceidg_rej_rb = tk.Radiobutton(
            adresy_frame, variable=self.rej_var, value=0,
            command=lambda: self.ukryj(None, None))
        ceidg_rej_rb.grid(row=1, column=1)

        # Adr1 REJESTROWY
        adr1_rej_rb = tk.Radiobutton(
            adresy_frame, variable=self.rej_var, value=1,
            command=lambda: self.ukryj(self.adr_1_entry, self.rej_var))
        adr1_rej_rb.grid(row=2, column=1)

        # Adr2 REJESTROWY
        adr2_rej_rb = tk.Radiobutton(
            adresy_frame, variable=self.rej_var, value=2,
            command=lambda: self.ukryj(self.adr_2_entry, self.rej_var))
        adr2_rej_rb.grid(row=3, column=1)

        # Adr3 REJESTROWY
        adr3_rej_rb = tk.Radiobutton(
            adresy_frame, variable=self.rej_var, value=3,
            command=lambda: self.ukryj(self.adr_3_entry, self.rej_var))
        adr3_rej_rb.grid(row=4, column=1)

        # KORESPONDENCJI

        # Ceidg KORESPONDENCJI
        ceidg_kor_rb = tk.Radiobutton(
            adresy_frame, variable=self.kor_var, value=0,
            command=lambda: self.ukryj(None, None))
        ceidg_kor_rb.grid(row=1, column=2)

        # Adr1 KORESPONDENCJI
        adr1_kor_rb = tk.Radiobutton(
            adresy_frame, variable=self.kor_var, value=1,
            command=lambda: self.ukryj(self.adr_1_entry, self.kor_var))
        adr1_kor_rb.grid(row=2, column=2)

        # Adr2 KORESPONDENCJI
        adr2_kor_rb = tk.Radiobutton(
            adresy_frame, variable=self.kor_var, value=2,
            command=lambda: self.ukryj(self.adr_2_entry, self.kor_var))
        adr2_kor_rb.grid(row=3, column=2)

        # Adr3 KORESPONDENCJI
        adr3_kor_rb = tk.Radiobutton(
            adresy_frame, variable=self.kor_var, value=3,
            command=lambda: self.ukryj(self.adr_3_entry, self.kor_var))
        adr3_kor_rb.grid(row=4, column=2)

        # DOSTARCZENIA

        # Ceidg DOSTARCZENIA
        ceidg_dost_rb = tk.Radiobutton(
            adresy_frame, variable=self.dost_var, value=0,
            command=lambda: self.ukryj(None, None))
        ceidg_dost_rb.grid(row=1, column=3)

        # Adr1 DOSTARCZENIA
        adr1_dost_rb = tk.Radiobutton(
            adresy_frame, variable=self.dost_var, value=1,
            command=lambda: self.ukryj(self.adr_1_entry, self.dost_var))
        adr1_dost_rb.grid(row=2, column=3)

        # Adr2 DOSTARCZENIA
        adr2_dost_rb = tk.Radiobutton(
            adresy_frame, variable=self.dost_var, value=2,
            command=lambda: self.ukryj(self.adr_2_entry, self.dost_var))
        adr2_dost_rb.grid(row=3, column=3)

        # Adr3 DOSTARCZENIA
        adr3_dost_rb = tk.Radiobutton(
            adresy_frame, variable=self.dost_var, value=3,
            command=lambda: self.ukryj(self.adr_3_entry, self.dost_var))
        adr3_dost_rb.grid(row=4, column=3)

        # Zaznacz wszystko CEIDG
        ceidg_rej_rb.select()
        ceidg_kor_rb.select()
        ceidg_dost_rb.select()

        # Adresy entry
        # CEIDG
        ceidg_label = tk.Label(adresy_frame,
                               text='Adres taki sam jak rejestrowy w CEIDG',
                               font=font10b)
        ceidg_label.grid(row=1, column=0, padx=(0,20), pady=7)
        # Adres 1
        self.adr_1_entry = tk.Entry(
            adresy_frame, width=entry_width, state='disabled',
            disabledbackground='#C0C0C0', borderwidth=brwid, font=font9)
        self.adr_1_entry.grid(row=2, column=0, pady=7)
        # Adres 2
        self.adr_2_entry = tk.Entry(
            adresy_frame, width=entry_width, state='disabled',
            disabledbackground='#C0C0C0', borderwidth=brwid, font=font9)
        self.adr_2_entry.grid(row=3, column=0, pady=7)
        # Adres 3
        self.adr_3_entry = tk.Entry(
            adresy_frame, width=entry_width, state='disabled',
            disabledbackground='#C0C0C0', borderwidth=brwid, font=font9)
        self.adr_3_entry.grid(row=4, column=0, pady=7)


        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=100, column=0)


        # Branża
        branza = tk.Label(left_frame, text='Branża:', font=font10b)
        branza.grid(row=0, column=2, padx=(20,10))
        self.branza_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.branza_entry.grid(row=0, column=3)

        # Pytania do prawnika
        pytania = tk.Label(
            left_frame, text='Pytania:', font=font10b)
        pytania.grid(row=10, column=2, padx=(20,10))
        self.pytania_entry = tk.Entry(left_frame, width=entry_width, borderwidth=brwid, font=font9)
        self.pytania_entry.grid(row=10, column=3)

        # Dodatkowe informacje
        dodatkowe = tk.Label(
            left_frame, text='Dodatkowe\ninformacje:', font=font10b)
        dodatkowe.grid(row=20, column=2, padx=(20,10), rowspan=30)
        self.dodatkowe_entry = ScrolledText(
            left_frame, width=entry_width-2, height=5, borderwidth=brwid, font=font9)
        self.dodatkowe_entry.grid(row=20, column=3, rowspan=30)
        self.dodatkowe_entry.bind_class(
            'Text', '<Button-3><ButtonRelease-3>', self.show_menu)


        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=140, column=0)

        # Załącznik
        zalacznik = tk.Button(left_frame, text='Załącznik', font=font10, width=12, padx=10,
                              command=lambda: self.zal_butt())
        zalacznik.grid(row=150, column=0)
        self.zal_label = tk.Label(left_frame, text='', font=font10b)
        self.zal_label.grid(row=151, column=0)

        # Wyślij
        wyslij = tk.Button(left_frame, text='Wyślij', font=font10, width=12, padx=10,
                           command=lambda: self.wyslij_butt())
        wyslij.grid(row=150, column=1)


        rozne_frame.pack(side=tk.BOTTOM, pady=(0, 10))
        left_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 20))
        right_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        menu_frame.pack(fill=tk.BOTH, expand=True, padx=(0, 20))
        page_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

if __name__ == '__main__':
    konsultant.kto = 'Developer ON'
    umowa = Umowa('Goldwin Mailsender')
