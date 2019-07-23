'''Główna klasa window, z której inne inheritują.
Tutaj ustawia się: tytuł, rozmiar, umieszczenie okna na środku ekranu.
Funkcja create frames jest pusta, klasa która inherituje musi nadpisać
funkcję createframes, tam ustawia się widgety.'''

import tkinter as tk
import sys
from config import dodatkowi_odbiorcy, entry_width, font10


class Window():
    def __init__(self, title, size):
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

        self.widgets()

        self.root.mainloop()  # główny loop

    def widgets(self):
        pass

    def dod_butt(self):
        top = tk.Toplevel()
        top.title("Dodaj odbiorców")
        top.geometry('250x150')
        top.tk.call('wm', 'iconphoto',
                    top._w, tk.PhotoImage(file='pliki/ikona.gif'))

        '''Ustawienie na środku ekranu oraz ikonka.'''
        # top.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
        top.tk.call('wm', 'iconphoto', top._w,
                          tk.PhotoImage(file='pliki/ikona.gif'))
        top.update_idletasks()
        width = top.winfo_width()
        height = top.winfo_height()
        x = (top.winfo_screenwidth() // 2) - (width // 2)
        y = (top.winfo_screenheight() // 2) - (height // 2)
        top.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        adresy_frame = tk.Frame(top)
        adresy_frame.pack()

        adres1 = tk.Entry(adresy_frame, width=entry_width)
        adres1.pack(pady=5)
        adres1.insert(tk.END, dodatkowi_odbiorcy[0])

        adres2 = tk.Entry(adresy_frame, width=entry_width)
        adres2.pack(pady=5)
        adres2.insert(tk.END, dodatkowi_odbiorcy[1])

        adres3 = tk.Entry(adresy_frame, width=entry_width)
        adres3.pack(pady=5)
        adres3.insert(tk.END, dodatkowi_odbiorcy[2])

        ok_butt = tk.Button(top, text="Zapisz",
                            font=font10, width=10,
                            command=lambda: wez_adresy())
        ok_butt.pack()


    def menu_butt(self):
        self.root.destroy()
