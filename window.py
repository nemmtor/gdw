'''Główna klasa window, z której inne inheritują.
Tutaj ustawia się: tytuł, rozmiar, umieszczenie okna na środku ekranu.
Funkcja create frames jest pusta, klasa która inherituje musi nadpisać
funkcję createframes, tam ustawia się widgety.'''

import tkinter as tk
import sys
from config import entry_width, font10, konsultant


class Window():
    def __init__(self, title, size):
        '''Ustawienie tytułu, rozmiaru'''
        self.title = title
        self.size = size

        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.size)

        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
        self.root.tk.call('wm', 'iconphoto', self.root._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.widgets()  # widgety

        self.root.mainloop()  # główny loop

    def widgets(self):
        pass

    def dod_butt(self):
        self.top = tk.Toplevel()
        self.top.title("Dodaj odbiorców")
        self.top.geometry('250x150')
        self.top.tk.call('wm', 'iconphoto',
                    self.top._w, tk.PhotoImage(file='pliki/ikona.gif'))

        '''Ustawienie na środku ekranu oraz ikonka.'''
        self.top.protocol('WM_DELETE_WINDOW', lambda: self.wez_adresy())
        self.top.tk.call('wm', 'iconphoto', self.top._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
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
        self.adres1.insert(tk.END, konsultant.dod_odbiorcy[0])

        self.adres2 = tk.Entry(adresy_frame, width=entry_width)
        self.adres2.pack(pady=5)
        self.adres2.insert(tk.END, konsultant.dod_odbiorcy[1])

        self.adres3 = tk.Entry(adresy_frame, width=entry_width)
        self.adres3.pack(pady=5)
        self.adres3.insert(tk.END, konsultant.dod_odbiorcy[2])

        ok_butt = tk.Button(self.top, text="Zapisz",
                            font=font10, width=10,
                            command=lambda: self.wez_adresy())
        ok_butt.pack()

    def wez_adresy(self):
        '''Pobiera adresy z entry'''
        dodatkowi = [self.adres1.get(), self.adres2.get(), self.adres3.get()]
        konsultant.dodatkowi(dodatkowi)
        print(konsultant.dod_odbiorcy)
        self.top.destroy()

    def menu_butt(self):
        self.root.destroy()
