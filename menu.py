'''Okno menu.'''
from window import Window  # klasa okna
import tkinter as tk
from config import font10

# Obiekty
from konsultant import konsultant


class Menu(Window):

    # Funkcje przycisków:
    def menu_button(self, wybor):
        '''Wybór menu, następnie usunięcie okna menu.'''
        konsultant.menu(wybor)
        self.root.destroy()

    def widgets(self):
        '''Widgety'''

        # Główny frame
        page_frame = tk.Frame(self.root)

        # Informacja kto zalogowany
        # Label
        zalog_label = tk.Label(page_frame, text='Zalogowany jako:')
        # Label z imieniem i nazwiskiem
        kons_label = tk.Label(page_frame, text=konsultant.kto,
                              font=font10, fg='green')

        # Przycisk umowa
        umowa = tk.Button(page_frame, text='Umowa', font=font10,
                          height=2, width=18,
                          command=lambda: self.menu_button(1))

        # Przycisk sprawy nierozwiązane
        sprawy = tk.Button(page_frame, text='Sprawy nierozwiązane',
                           font=font10, height=2, width=18,
                           command=lambda: self.menu_button(2))

        # Przycisk aneks
        aneks = tk.Button(page_frame, text='Aneks', font=font10,
                          height=2, width=18,
                          command=lambda: self.menu_button(3))

        # Przycisk wypowiedzenie
        wypo = tk.Button(page_frame, text='Wypowiedzenie', font=font10,
                         height=2, width=18,
                         command=lambda: self.menu_button(4))


        # Pack
        zalog_label.pack()
        kons_label.pack()
        umowa.pack()
        sprawy.pack()
        aneks.pack()
        wypo.pack()
        page_frame.pack()
