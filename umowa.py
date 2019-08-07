'''Okno umowy.'''
from window import Window
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
from bezpolskich import stworz_plik_ascii
from config import font10, font10b, entry_width
from konsultant import konsultant
from mailsender import mailsender

from config import ikona, goldwin


class Umowa(Window):
    '''frame = entry frame'''

    def dod_butt(self):
        self.top = tk.Toplevel()
        self.top.title("Dodaj odbiorców")
        self.top.geometry('250x150')
        self.top.tk.call('wm', 'iconphoto',
                         self.top._w, tk.PhotoImage(file=ikona))

        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.top.protocol('WM_DELETE_WINDOW', lambda: self.wez_adresy())
        self.top.tk.call('wm', 'iconphoto', self.top._w,
                         tk.PhotoImage(file=ikona))
        self.top.update_idletasks()
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        x = (self.top.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top.winfo_screenheight() // 2) - (height // 2)
        self.top.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Dodatkowe adresy
        adresy_frame = tk.Frame(self.top)
        adresy_frame.pack()

        self.adres1 = tk.Entry(adresy_frame, width=entry_width)
        self.adres1.pack(pady=5)
        self.adres1.insert(tk.END, mailsender.dod_odbiorcy[0])

        self.adres2 = tk.Entry(adresy_frame, width=entry_width)
        self.adres2.pack(pady=5)
        self.adres2.insert(tk.END, mailsender.dod_odbiorcy[1])

        self.adres3 = tk.Entry(adresy_frame, width=entry_width)
        self.adres3.pack(pady=5)
        self.adres3.insert(tk.END, mailsender.dod_odbiorcy[2])

        ok_butt = tk.Button(self.top, text="Zapisz",
                            font=font10, width=10,
                            command=lambda: self.wez_adresy())
        ok_butt.pack()

    def wez_adresy(self):
        '''Pobiera adresy z entry'''
        mailsender.dod_odbiorcy = [
            self.adres1.get(), self.adres2.get(), self.adres3.get()]
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
            mailsender.zalacznik = stworz_plik_ascii(mailsender.zalacznik)
            self.zal_label.configure(text=mailsender.zalacznik, fg='green')

    def ukryj(self, entry, var):
        '''Funkcja blokowania entry adresów.'''
        if var.get():
            entry.config(state='disabled')
        else:
            entry.config(state='normal')

    def widgets(self):
        '''Widgety.'''
        page_frame = tk.Frame(self.root)

        left_frame = tk.Frame(page_frame)
        # mid_frame = tk.Frame(page_frame, bg='green')
        right_frame = tk.Frame(page_frame)
        menu_frame = tk.Frame(page_frame)
        left_frame.pack(fill=tk.BOTH, expand=False, side=tk.LEFT)
        # mid_frame.pack(fill=tk.BOTH, expan=True, side=tk.LEFT)
        right_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        menu_frame.pack(fill=tk.BOTH, expand=True)

        # MENU FRAME (po prawej stronie)
        zalog_label = tk.Label(menu_frame, text='Zalogowany jako:')
        zalog_label.pack(pady=10)
        kons_label = tk.Label(menu_frame, text=konsultant.kto,
                              font=('Arial 800', 10), fg='green')
        kons_label.pack()

        menu_button = tk.Button(menu_frame, text="MENU",
                                font=font10, width=10,
                                command=lambda: self.menu_butt())
        menu_button.pack(pady=20)

        dod_adresy_button = tk.Button(menu_frame, text="Dodaj odbiorce",
                                      font=font10, width=10,
                                      command=lambda: self.dod_butt())
        dod_adresy_button.pack()

        sprawy_frame = tk.Frame(menu_frame)

        spr_nierozw_label = tk.Label(sprawy_frame, text='Sprawy nierozwiązane')
        self.spr_nierozw_var = tk.IntVar(value=0)
        self.spr_nierozw_cb = tk.Checkbutton(sprawy_frame,
                                             variable=self.spr_nierozw_var,
                                             command=lambda: self.zmienvar())
        self.spr_nierozw_cb.pack(side=tk.LEFT)
        spr_nierozw_label.pack()
        sprawy_frame.pack(pady=20)

        # MID FRAME
        img = tk.PhotoImage(file=goldwin)
        img_Label = tk.Label(right_frame, image=img)
        img_Label.image = img
        img_Label.place(relx=.5, rely=.5, anchor="c")

        # LEFT FRAME

        # Imie i nazwisko
        imie = tk.Label(left_frame, text="Imię i nazwisko:", font=font10b)
        imie.grid(row=0, column=0)
        self.imie_entry = tk.Entry(left_frame, width=entry_width)
        self.imie_entry.grid(row=0, column=1, sticky='E')

        # Numer telefonu
        tel = tk.Label(left_frame, text="Numer telefonu:", font=font10b)
        tel.grid(row=10, column=0)
        self.tel_entry = tk.Entry(left_frame, width=entry_width)
        self.tel_entry.grid(row=10, column=1)

        # Data sprzedaży
        sprz = tk.Label(left_frame, text="Data sprzedaży:", font=font10b)
        sprz.grid(row=20, column=0)
        self.sprz_entry = tk.Entry(left_frame, width=entry_width)
        self.sprz_entry.grid(row=20, column=1)

        # Date dostarczenia
        dost = tk.Label(left_frame, text="Data dostarczenia:", font=font10b)
        dost.grid(row=30, column=0)
        self.dost_entry = tk.Entry(left_frame, width=entry_width)
        self.dost_entry.grid(row=30, column=1)

        # Cena
        cena = tk.Label(
            left_frame, text="Cena/długość zobowiązania:", font=font10b)
        cena.grid(row=40, column=0)
        self.cena_entry = tk.Entry(left_frame, width=entry_width)
        self.cena_entry.grid(row=40, column=1)

        # Adres mailowy
        mail = tk.Label(left_frame, text="Adres mailowy", font=font10b)
        mail.grid(row=50, column=0)
        self.mail_entry = tk.Entry(left_frame, width=entry_width)
        self.mail_entry.grid(row=50, column=1)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=60, column=0)

        # Adres rejestrowy
        adr_rej = tk.Label(left_frame, text="Adres rejestrowy", font=font10b)
        adr_rej.grid(row=70, column=0)
        self.adr_rej_entry = tk.Entry(
            left_frame, width=entry_width, state='disabled')
        self.adr_rej_entry.grid(row=70, column=1)
        # Checkbox
        self.adr_rej_var = tk.IntVar(value=1)
        adr_rej_cb = tk.Checkbutton(left_frame, variable=self.adr_rej_var,
                                    command=lambda:
                                    self.ukryj(self.adr_rej_entry,
                                               self.adr_rej_var))
        adr_rej_cb.select()
        adr_rej_cb.grid(row=70, column=2)

        # Adres adr_korespondencyjny
        adr_kor = tk.Label(
            left_frame, text="Adres korespondencyjny", font=font10b)
        adr_kor.grid(row=80, column=0)
        self.adr_kor_entry = tk.Entry(
            left_frame, width=entry_width, state='disabled')
        self.adr_kor_entry.grid(row=80, column=1)
        # Checkbox
        self.adr_kor_var = tk.IntVar(value=1)
        adr_kor_cb = tk.Checkbutton(left_frame, variable=self.adr_kor_var,
                                    command=lambda:
                                    self.ukryj(self.adr_kor_entry,
                                               self.adr_kor_var))
        adr_kor_cb.select()
        adr_kor_cb.grid(row=80, column=2)

        # Adres dostarczenia
        adr_dost = tk.Label(
            left_frame, text="Adres dostarczenia", font=font10b)
        adr_dost.grid(row=90, column=0)
        self.adr_dost_entry = tk.Entry(
            left_frame, width=entry_width, state='disabled')
        self.adr_dost_entry.grid(row=90, column=1)
        # Checkbox
        self.adr_dost_var = tk.IntVar(value=1)
        adr_dost_cb = tk.Checkbutton(left_frame, variable=self.adr_dost_var,
                                     command=lambda:
                                     self.ukryj(self.adr_dost_entry,
                                                self.adr_dost_var))
        adr_dost_cb.select()
        adr_dost_cb.grid(row=90, column=2)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=100, column=0)
        page_frame.pack(fill=tk.BOTH, expand=True)

        # Branża
        branza = tk.Label(left_frame, text="Branża:", font=font10b)
        branza.grid(row=110, column=0)
        self.branza_entry = tk.Entry(left_frame, width=entry_width)
        self.branza_entry.grid(row=110, column=1)

        # Pytania do prawnika
        pytania = tk.Label(
            left_frame, text="Pytania do prawnika:", font=font10b)
        pytania.grid(row=120, column=0)
        self.pytania_entry = tk.Entry(left_frame, width=entry_width)
        self.pytania_entry.grid(row=120, column=1)

        # Dodatkowe informacje
        dodatkowe = tk.Label(
            left_frame, text="Dodatkowe informacje:", font=font10b)
        dodatkowe.grid(row=130, column=0)
        self.dodatkowe_entry = ScrolledText(
            left_frame, width=entry_width - 7, height=2)
        self.dodatkowe_entry.grid(row=130, column=1)

        # Spacer
        spacer = tk.Label(left_frame)
        spacer.grid(row=140, column=0)

        # Załącznik
        zalacznik = tk.Button(left_frame, text="Załącznik", font=font10b,
                              command=lambda: self.zal_butt())
        zalacznik.grid(row=150, column=0)
        self.zal_label = tk.Label(left_frame, text='', font=font10b)
        self.zal_label.grid(row=151, column=0, columnspan=1)

        # Wyślij
        wyslij = tk.Button(left_frame, text="Wyślij", font=font10b,
                           command=lambda: self.wyslij_butt())
        wyslij.grid(row=150, column=1)

        page_frame.pack(fill=tk.BOTH, expand=True)
